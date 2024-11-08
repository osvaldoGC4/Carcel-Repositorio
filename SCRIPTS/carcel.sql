-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-11-2024 a las 21:56:11
-- Versión del servidor: 10.4.19-MariaDB
-- Versión de PHP: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `carcel`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `ContarReclusosPorCelda` ()  BEGIN
    SELECT 
        c.Ubicacion,
        COUNT(i.ID_Interno) AS Total_Reclusos
    FROM 
        celda c
    LEFT JOIN 
        interno i ON c.ID_Celda = i.ID_Celda
    GROUP BY 
        c.ID_Celda;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ObtenerCondenaPorInternoYDelito` (IN `p_ID_Interno` INT, IN `p_ID_Delito` INT)  BEGIN
    SELECT 
        c.ID_Condena,
        c.Fecha_Inicio,
        c.Duracion,
        c.Tipo,
        i.Nombre AS Nombre_Interno,
        d.Tipo AS Tipo_Delito
    FROM 
        condena c
    INNER JOIN 
        interno i ON c.ID_Interno = i.ID_Interno
    INNER JOIN 
        delito d ON c.ID_Delito = d.ID_Delito
    WHERE 
        c.ID_Interno = p_ID_Interno AND c.ID_Delito = p_ID_Delito;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteCelda` (IN `p_condition` VARCHAR(255))  BEGIN
    SET @query = CONCAT('DELETE FROM celda WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_InsertCelda` (IN `p_celda_json` JSON)  BEGIN
    DECLARE v_id_celda INT;
    DECLARE v_ubicacion VARCHAR(255);
    DECLARE v_capacidad INT;
    DECLARE v_estado VARCHAR(50);

    -- Extraer los valores del JSON recibido
    SET v_id_celda = JSON_UNQUOTE(JSON_EXTRACT(p_celda_json, '$.ID'));
    SET v_ubicacion = JSON_UNQUOTE(JSON_EXTRACT(p_celda_json, '$.Ubicacion'));
    SET v_capacidad = JSON_UNQUOTE(JSON_EXTRACT(p_celda_json, '$.Capacidad'));
    SET v_estado = JSON_UNQUOTE(JSON_EXTRACT(p_celda_json, '$.Estado'));

    -- Verificar si se proporcionó un ID
    IF v_id_celda IS NOT NULL THEN
        -- Verificar si ya existe una celda con el mismo ID
        IF EXISTS (SELECT 1 FROM celda WHERE ID = v_id_celda) THEN
            -- Lanzar un error personalizado, pero devolverlo como un SELECT
            SELECT 'Error' AS Status, 'El ID_Celda ya existe. No se puede insertar.' AS Message;
        ELSE
            -- Insertar nueva celda con el ID proporcionado
            INSERT INTO celda (ID, Ubicacion, Capacidad, Estado) 
            VALUES (v_id_celda, v_ubicacion, v_capacidad, v_estado);
            COMMIT;
            -- Devolver la fila insertada
            SELECT * FROM celda WHERE ID = v_id_celda;
        END IF;
    ELSE
        -- Insertar nueva celda sin ID (ID autogenerado si es una PK auto_increment)
        INSERT INTO celda (Ubicacion, Capacidad, Estado) 
        VALUES (v_ubicacion, v_capacidad, v_estado);
		COMMIT;
        -- Obtener el ID generado automáticamente y devolver la fila insertada
        SET v_id_celda = LAST_INSERT_ID();
        SELECT * FROM celda WHERE ID = v_id_celda;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectCelda` (IN `p_id` INT)  BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        -- Si no se pasa un ID o se pasa un valor que represente "todos"
        SELECT * FROM celda;
    ELSE
        -- Si se pasa un ID válido
        SELECT * FROM celda WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Updatecelda` (IN `p_UpdateJSON` JSON, IN `p_ConditionJSON` JSON)  BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Manejo de errores SQL
        ROLLBACK;
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Error al ejecutar la actualización. Verifique los datos.';
    END;

    DECLARE EXIT HANDLER FOR SQLWARNING
    BEGIN
        -- Manejo de advertencias SQL
        ROLLBACK;
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Advertencia durante la ejecución.';
    END;

    START TRANSACTION;

    -- Depuración: Mostrar el JSON de condición
    SELECT CONCAT('Condición WHERE: ', JSON_UNQUOTE(JSON_EXTRACT(p_ConditionJSON, '$.where')));

    -- Construir la cláusula WHERE a partir del JSON
    SET @where_clause = JSON_UNQUOTE(JSON_EXTRACT(p_ConditionJSON, '$.where'));

    -- Verificar si existe un registro con la condición especificada
    SET @check_sql = CONCAT('SELECT COUNT(*) INTO @row_exists FROM celda WHERE ', @where_clause);
    PREPARE stmt_check FROM @check_sql;
    EXECUTE stmt_check;
    DEALLOCATE PREPARE stmt_check;

    IF @row_exists = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró un registro con la condición especificada.';
    END IF;

    -- Construir dinámicamente la cláusula SET para la actualización
    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(
                COLUMN_NAME, ' = ', 
                QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))
            ) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'celda'
          AND COLUMN_NAME NOT IN (REPLACE(JSON_UNQUOTE(JSON_EXTRACT(p_ConditionJSON, '$.where')), 'ID = ', ''))
    );

    -- Depuración: Ver la cláusula SET generada
    SELECT CONCAT('Cláusula SET: ', @set_clause);

    -- Construir la consulta de actualización
    SET @update_sql = CONCAT('UPDATE celda SET ', @set_clause, ' WHERE ', @where_clause);
    -- Depuración: Ver la consulta generada
    SELECT CONCAT('Consulta SQL Generada: ', @update_sql);

    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    -- Verificar si se actualizó algún registro
    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        -- Retornar el registro actualizado
        SET @result_sql = CONCAT('SELECT * FROM celda WHERE ', @where_clause);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividad`
--

CREATE TABLE `actividad` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Tipo` varchar(255) DEFAULT NULL COMMENT 'Educativa, Recreativa, Laboral',
  `Horario` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `actividad`
--

INSERT INTO `actividad` (`ID`, `Nombre`, `Tipo`, `Horario`) VALUES
(1, 'Actividad Cultural', 'Deporte', '09:00-10:00'),
(2, 'Clases de Matemáticas', 'Educativa', '11:00-13:00'),
(3, 'Cuidado del Huerto', 'Laboral', '14:00-16:00'),
(4, 'Yoga', 'Recreativa', '16:00-17:00'),
(5, 'Terapia Ocupacional', 'Educativa', '10:00-12:00'),
(6, 'Deportes', 'Recreativa', '15:00-17:00'),
(7, 'Clases de Música', 'Educativa', '09:00-11:00'),
(8, 'Cocina', 'Laboral', '12:00-14:00'),
(9, 'Entrenamiento Físico', 'Recreativa', '08:00-09:00'),
(10, 'Taller de Escritura', 'Educativa', '13:00-15:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `celda`
--

CREATE TABLE `celda` (
  `ID` int(11) NOT NULL,
  `Ubicacion` varchar(255) DEFAULT NULL,
  `Capacidad` int(11) DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL COMMENT 'Ocupada, Disponible'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `celda`
--

INSERT INTO `celda` (`ID`, `Ubicacion`, `Capacidad`, `Estado`) VALUES
(1, 'Medellin', 8, 'Disponible'),
(2, 'Medellin2', 5, 'Disponible'),
(3, 'Bello', 10, 'Disponible'),
(4, 'Aranjuez', 100, 'Disponible'),
(5, 'Zona Centro', 60, 'Disponible'),
(6, 'Zona Alta', 70, 'Ocupada'),
(7, 'Zona Baja', 80, 'Disponible'),
(8, 'Zona Interior', 55, 'Ocupada'),
(9, 'Zona de Aislamiento', 15, 'Disponible'),
(10, 'Zona Familiar', 20, 'Ocupada'),
(11, 'Choco', 24, 'Disponible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `condena`
--

CREATE TABLE `condena` (
  `ID` int(11) NOT NULL,
  `ID_Interno` int(11) DEFAULT NULL,
  `ID_Delito` int(11) DEFAULT NULL,
  `Fecha_Inicio` date DEFAULT NULL,
  `Duracion` int(11) DEFAULT NULL COMMENT 'En meses',
  `Tipo` varchar(255) DEFAULT NULL COMMENT 'Ejemplo: Permanente, Temporal',
  `ID_Personal` int(11) DEFAULT NULL COMMENT 'Responsable de la condena'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `condena`
--

INSERT INTO `condena` (`ID`, `ID_Interno`, `ID_Delito`, `Fecha_Inicio`, `Duracion`, `Tipo`, `ID_Personal`) VALUES
(1, 1, 1, '2023-01-01', 12, 'Permanente', 1),
(2, 2, 2, '2022-06-15', 6, 'Temporal', 2),
(3, 3, 3, '2023-03-20', 24, 'Permanente', 3),
(4, 4, 1, '2024-01-10', 18, 'Temporal', 1),
(5, 5, 2, '2022-11-05', 30, 'Permanente', 2),
(6, 6, 3, '2023-05-25', 36, 'Temporal', 3),
(7, 7, 1, '2024-04-15', 24, 'Permanente', 1),
(8, 8, 2, '2022-08-30', 12, 'Temporal', 2),
(9, 9, 3, '2023-12-12', 48, 'Permanente', 3),
(10, 10, 1, '2024-02-20', 6, 'Temporal', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `delito`
--

CREATE TABLE `delito` (
  `ID` int(11) NOT NULL,
  `Tipo` varchar(255) DEFAULT NULL,
  `Descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `delito`
--

INSERT INTO `delito` (`ID`, `Tipo`, `Descripcion`) VALUES
(1, 'Mano armada', 'Puñalada en un ojo'),
(2, 'asesinato', 'fleteo'),
(3, 'corrupcion', 'abogado'),
(4, 'Tráfico de drogas', 'Tráfico de sustancias controladas'),
(5, 'Secuestro', 'Secuestro de personas'),
(6, 'Extorsión', 'Extorsión económica'),
(7, 'Destrucción de propiedad', 'Destrucción intencional de bienes'),
(8, 'Cibercrimen', 'Delitos informáticos'),
(9, 'Homicidio culposo', 'Causar la muerte sin intención'),
(10, 'Lesiones', 'Causar daño físico a una persona');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informedisciplina`
--

CREATE TABLE `informedisciplina` (
  `ID` int(11) NOT NULL,
  `ID_Interno` int(11) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Descripcion` text DEFAULT NULL,
  `Sancion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `informedisciplina`
--

INSERT INTO `informedisciplina` (`ID`, `ID_Interno`, `Fecha`, `Descripcion`, `Sancion`) VALUES
(1, 1, '2024-01-15', 'Riña con otro interno', 'Reprimenda'),
(2, 2, '2024-01-16', 'Fuga tentativa', 'Aislamiento'),
(3, 3, '2024-01-17', 'Uso de drogas', 'Suspensión de actividades'),
(4, 4, '2024-01-18', 'Desobediencia', 'Trabajo forzado'),
(5, 5, '2024-01-19', 'Amenaza a personal', 'Aislamiento'),
(6, 6, '2024-01-20', 'Destrucción de bienes', 'Reparación de daños'),
(7, 7, '2024-01-21', 'Robo de alimentos', 'Aumento de horas de trabajo'),
(8, 8, '2024-01-22', 'Consumo de alcohol', 'Reprimenda'),
(9, 9, '2024-01-23', 'Insubordinación', 'Suspensión de visitas'),
(10, 10, '2024-01-24', 'Alteración del orden', 'Aislamiento');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `interno`
--

CREATE TABLE `interno` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Fecha_Ingreso` date DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL COMMENT 'Activo, Liberado, Transferido',
  `ID_Celda` int(11) DEFAULT NULL,
  `Fecha_Liberacion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `interno`
--

INSERT INTO `interno` (`ID`, `Nombre`, `Fecha_Ingreso`, `Estado`, `ID_Celda`, `Fecha_Liberacion`) VALUES
(1, 'Juan Perez', '2023-01-01', 'Liberado', 2, '0000-00-00'),
(2, 'Luis Gómez', '2021-06-15', 'Activo', 2, NULL),
(3, 'Carlos Fernández', '2023-03-20', 'Activo', 3, NULL),
(4, 'José Martínez', '2024-01-10', 'Activo', 4, NULL),
(5, 'Ana Torres', '2022-11-05', 'Liberado', 5, '2024-01-01'),
(6, 'María López', '2023-05-25', 'Activo', 6, NULL),
(7, 'Jorge Santos', '2024-04-15', 'Activo', 7, NULL),
(8, 'Ricardo Alvarado', '2022-08-30', 'Transferido', 8, NULL),
(9, 'Sofía Morales', '2023-12-12', 'Activo', 9, NULL),
(10, 'Isabel Sánchez', '2024-02-20', 'Liberado', 10, '2024-03-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `internoactividad`
--

CREATE TABLE `internoactividad` (
  `ID` int(11) NOT NULL,
  `ID_Interno` int(11) NOT NULL,
  `ID_Actividad` int(11) NOT NULL,
  `Fecha_Actividad` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `internoactividad`
--

INSERT INTO `internoactividad` (`ID`, `ID_Interno`, `ID_Actividad`, `Fecha_Actividad`) VALUES
(1, 1, 1, '2024-02-02'),
(2, 1, 2, '2024-02-02'),
(3, 2, 1, '2024-02-02'),
(4, 2, 3, '2024-02-02'),
(5, 3, 2, '2024-02-02'),
(6, 3, 4, '2024-02-02'),
(7, 4, 3, '2024-02-02'),
(8, 5, 2, '2024-02-02'),
(9, 6, 5, '2024-02-02'),
(10, 7, 6, '2024-02-02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal`
--

CREATE TABLE `personal` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Rol` varchar(255) DEFAULT NULL COMMENT 'Ejemplo: Guardia, Administrador',
  `Horario` varchar(255) DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL COMMENT 'Activo, Inactivo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `personal`
--

INSERT INTO `personal` (`ID`, `Nombre`, `Rol`, `Horario`, `Estado`) VALUES
(1, 'Andru00e9s Ruiz', 'Guardia', '08:00-16:00', 'Inactivo'),
(2, 'Paola Martínez', 'Administradora', '09:00-17:00', 'Activo'),
(3, 'Fernando Gómez', 'Psicólogo', '10:00-18:00', 'Activo'),
(4, 'Laura Fernández', 'Educadora', '09:00-17:00', 'Inactivo'),
(5, 'Carlos Sánchez', 'Guardia', '08:00-16:00', 'Activo'),
(6, 'Julián Castro', 'Administradora', '09:00-17:00', 'Inactivo'),
(7, 'Elena Pérez', 'Psicóloga', '10:00-18:00', 'Activo'),
(8, 'Marisol López', 'Educadora', '09:00-17:00', 'Activo'),
(9, 'Ricardo Morales', 'Guardia', '08:00-16:00', 'Activo'),
(10, 'Sofia Torres', 'Administradora', '09:00-17:00', 'Activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transferencia`
--

CREATE TABLE `transferencia` (
  `ID` int(11) NOT NULL,
  `ID_Interno` int(11) DEFAULT NULL,
  `ID_Celda_Origen` int(11) DEFAULT NULL,
  `ID_Celda_Destino` int(11) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Motivo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `transferencia`
--

INSERT INTO `transferencia` (`ID`, `ID_Interno`, `ID_Celda_Origen`, `ID_Celda_Destino`, `Fecha`, `Motivo`) VALUES
(1, 1, 1, 2, '2024-01-01', NULL),
(2, 2, 2, 3, '2024-02-01', NULL),
(3, 3, 3, 4, '2024-03-01', NULL),
(4, 4, 4, 5, '2024-04-01', NULL),
(5, 5, 5, 6, '2024-05-01', NULL),
(6, 6, 6, 7, '2024-06-01', NULL),
(7, 7, 7, 8, '2024-07-01', NULL),
(8, 8, 8, 9, '2024-08-01', NULL),
(9, 9, 9, 10, '2024-09-01', NULL),
(10, 10, 10, 1, '2024-10-01', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visita`
--

CREATE TABLE `visita` (
  `ID` int(11) NOT NULL,
  `ID_Interno` int(11) DEFAULT NULL,
  `ID_Visitante` int(11) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Hora_Inicio` time DEFAULT NULL,
  `Duracion` int(11) DEFAULT NULL COMMENT 'En minutos'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `visita`
--

INSERT INTO `visita` (`ID`, `ID_Interno`, `ID_Visitante`, `Fecha`, `Hora_Inicio`, `Duracion`) VALUES
(1, 1, 2, '2024-11-08', '10:00:00', 401);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitamultiple`
--

CREATE TABLE `visitamultiple` (
  `ID` int(11) NOT NULL,
  `ID_Visita` int(11) NOT NULL,
  `ID_Visitante` int(11) NOT NULL,
  `Observacion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `visitamultiple`
--

INSERT INTO `visitamultiple` (`ID`, `ID_Visita`, `ID_Visitante`, `Observacion`) VALUES
(2, 1, 2, 'Mal comportamiento, agresivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitante`
--

CREATE TABLE `visitante` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Relacion` varchar(255) DEFAULT NULL COMMENT 'Ejemplo: Familiar, Abogado',
  `Documento` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `visitante`
--

INSERT INTO `visitante` (`ID`, `Nombre`, `Relacion`, `Documento`) VALUES
(2, 'John Valencia', 'Parcero', '1003222');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `celda`
--
ALTER TABLE `celda`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `condena`
--
ALTER TABLE `condena`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Interno` (`ID_Interno`),
  ADD KEY `ID_Delito` (`ID_Delito`),
  ADD KEY `ID_Personal` (`ID_Personal`);

--
-- Indices de la tabla `delito`
--
ALTER TABLE `delito`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `informedisciplina`
--
ALTER TABLE `informedisciplina`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Interno` (`ID_Interno`);

--
-- Indices de la tabla `interno`
--
ALTER TABLE `interno`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Celda` (`ID_Celda`);

--
-- Indices de la tabla `internoactividad`
--
ALTER TABLE `internoactividad`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Actividad` (`ID_Actividad`),
  ADD KEY `internoActividad_ibfk_1` (`ID_Interno`);

--
-- Indices de la tabla `personal`
--
ALTER TABLE `personal`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `transferencia`
--
ALTER TABLE `transferencia`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Interno` (`ID_Interno`),
  ADD KEY `ID_Celda_Origen` (`ID_Celda_Origen`),
  ADD KEY `ID_Celda_Destino` (`ID_Celda_Destino`);

--
-- Indices de la tabla `visita`
--
ALTER TABLE `visita`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Interno` (`ID_Interno`),
  ADD KEY `ID_Visitante` (`ID_Visitante`);

--
-- Indices de la tabla `visitamultiple`
--
ALTER TABLE `visitamultiple`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID_Visitante` (`ID_Visitante`),
  ADD KEY `ID_Visita` (`ID_Visita`);

--
-- Indices de la tabla `visitante`
--
ALTER TABLE `visitante`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `actividad`
--
ALTER TABLE `actividad`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `celda`
--
ALTER TABLE `celda`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `condena`
--
ALTER TABLE `condena`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `delito`
--
ALTER TABLE `delito`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `informedisciplina`
--
ALTER TABLE `informedisciplina`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `interno`
--
ALTER TABLE `interno`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `internoactividad`
--
ALTER TABLE `internoactividad`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `personal`
--
ALTER TABLE `personal`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `transferencia`
--
ALTER TABLE `transferencia`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `visita`
--
ALTER TABLE `visita`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `visitamultiple`
--
ALTER TABLE `visitamultiple`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `visitante`
--
ALTER TABLE `visitante`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `condena`
--
ALTER TABLE `condena`
  ADD CONSTRAINT `condena_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID`),
  ADD CONSTRAINT `condena_ibfk_2` FOREIGN KEY (`ID_Delito`) REFERENCES `delito` (`ID`),
  ADD CONSTRAINT `condena_ibfk_3` FOREIGN KEY (`ID_Personal`) REFERENCES `personal` (`ID`);

--
-- Filtros para la tabla `informedisciplina`
--
ALTER TABLE `informedisciplina`
  ADD CONSTRAINT `informeDisciplina_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID`);

--
-- Filtros para la tabla `interno`
--
ALTER TABLE `interno`
  ADD CONSTRAINT `interno_ibfk_1` FOREIGN KEY (`ID_Celda`) REFERENCES `celda` (`ID`);

--
-- Filtros para la tabla `internoactividad`
--
ALTER TABLE `internoactividad`
  ADD CONSTRAINT `internoActividad_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID`),
  ADD CONSTRAINT `internoActividad_ibfk_2` FOREIGN KEY (`ID_Actividad`) REFERENCES `actividad` (`ID`);

--
-- Filtros para la tabla `transferencia`
--
ALTER TABLE `transferencia`
  ADD CONSTRAINT `transferencia_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID`),
  ADD CONSTRAINT `transferencia_ibfk_2` FOREIGN KEY (`ID_Celda_Origen`) REFERENCES `celda` (`ID`),
  ADD CONSTRAINT `transferencia_ibfk_3` FOREIGN KEY (`ID_Celda_Destino`) REFERENCES `celda` (`ID`);

--
-- Filtros para la tabla `visita`
--
ALTER TABLE `visita`
  ADD CONSTRAINT `visita_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID`),
  ADD CONSTRAINT `visita_ibfk_2` FOREIGN KEY (`ID_Visitante`) REFERENCES `visitante` (`ID`);

--
-- Filtros para la tabla `visitamultiple`
--
ALTER TABLE `visitamultiple`
  ADD CONSTRAINT `visitaMultiple_ibfk_1` FOREIGN KEY (`ID_Visita`) REFERENCES `visita` (`ID`),
  ADD CONSTRAINT `visitaMultiple_ibfk_2` FOREIGN KEY (`ID_Visitante`) REFERENCES `visitante` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
