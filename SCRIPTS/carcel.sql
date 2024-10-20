-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-10-2024 a las 22:47:35
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

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
CREATE DEFINER=`root`@`localhost` PROCEDURE `DynamicalSelect` (IN `tableName` VARCHAR(255), IN `columnList` VARCHAR(255), IN `options` JSON)   BEGIN
    DECLARE sqlStatement TEXT;
    DECLARE whereClause TEXT DEFAULT '';
    DECLARE orderByClause TEXT DEFAULT '';
    DECLARE groupByClause TEXT DEFAULT '';
    DECLARE havingClause TEXT DEFAULT '';

    -- Construir la cláusula WHERE si existe
    IF JSON_UNQUOTE(JSON_EXTRACT(options, '$.where')) IS NOT NULL THEN
        SET whereClause = CONCAT(' WHERE ', JSON_UNQUOTE(JSON_EXTRACT(options, '$.where')));
    END IF;

    -- Construir la cláusula ORDER BY si existe
    IF JSON_UNQUOTE(JSON_EXTRACT(options, '$.order_by')) IS NOT NULL THEN
        SET orderByClause = CONCAT(' ORDER BY ', JSON_UNQUOTE(JSON_EXTRACT(options, '$.order_by')));
    END IF;

    -- Construir la cláusula GROUP BY si existe
    IF JSON_UNQUOTE(JSON_EXTRACT(options, '$.group_by')) IS NOT NULL THEN
        SET groupByClause = CONCAT(' GROUP BY ', JSON_UNQUOTE(JSON_EXTRACT(options, '$.group_by')));
    END IF;

    -- Construir la cláusula HAVING si existe
    IF JSON_UNQUOTE(JSON_EXTRACT(options, '$.having')) IS NOT NULL THEN
        SET havingClause = CONCAT(' HAVING ', JSON_UNQUOTE(JSON_EXTRACT(options, '$.having')));
    END IF;

    -- Construir la consulta SQL dinámica
    SET sqlStatement = CONCAT('SELECT ', columnList, ' FROM ', tableName, whereClause, groupByClause, havingClause, orderByClause);

    -- Ejecutar la consulta
    PREPARE stmt FROM sqlStatement;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `DynamicalUpdate` (IN `tableName` VARCHAR(255), IN `columnsAndValues` JSON, IN `options` JSON)   BEGIN
    DECLARE sqlStatement TEXT;
    DECLARE setClause TEXT DEFAULT '';
    DECLARE whereClause TEXT DEFAULT '';
    DECLARE errMsg TEXT;

    -- Validar que la tabla existe
    IF (SELECT COUNT(*) FROM information_schema.tables 
        WHERE table_name = tableName AND table_schema = DATABASE()) = 0 THEN
        SET errMsg = CONCAT('La tabla "', tableName, '" no existe.');
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = errMsg;
    END IF;

    -- Inicializar la cláusula SET
    SET setClause = '';

    -- Obtener las columnas de la tabla
    SELECT GROUP_CONCAT(column_name SEPARATOR ', ')
    INTO @columnList
    FROM information_schema.columns
    WHERE table_name = tableName AND table_schema = DATABASE();

    -- Verificar que se hayan obtenido columnas
    IF @columnList IS NULL THEN
        SET errMsg = CONCAT('No se encontraron columnas en la tabla "', tableName, '".');
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = errMsg;
    END IF;

    -- Construir la cláusula SET solo para las columnas que se envían
    SET @sqlSetClause = (
        SELECT GROUP_CONCAT(CONCAT(column_name, ' = ', 
            CASE 
                WHEN JSON_UNQUOTE(JSON_EXTRACT(columnsAndValues, CONCAT('$.', column_name))) IS NULL THEN 'NULL'
                ELSE QUOTE(JSON_UNQUOTE(JSON_EXTRACT(columnsAndValues, CONCAT('$.', column_name))))
            END
        ) SEPARATOR ', ')
        FROM information_schema.columns
        WHERE table_name = tableName AND table_schema = DATABASE()
          AND JSON_UNQUOTE(JSON_EXTRACT(columnsAndValues, CONCAT('$.', column_name))) IS NOT NULL
    );

    -- Validar que se hayan construido valores para el SET
    IF @sqlSetClause IS NULL OR @sqlSetClause = '' THEN
        SET errMsg = 'No se proporcionaron valores válidos para el UPDATE.';
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = errMsg;
    END IF;

    -- Construir la cláusula WHERE si existe
    IF JSON_UNQUOTE(JSON_EXTRACT(options, '$.where')) IS NOT NULL THEN
        SET whereClause = CONCAT(' WHERE ', JSON_UNQUOTE(JSON_EXTRACT(options, '$.where')));
    END IF;

    -- Crear la sentencia SQL dinámica
    SET sqlStatement = CONCAT('UPDATE ', tableName, ' SET ', @sqlSetClause, whereClause);

    -- Preparar y ejecutar la declaración
    PREPARE stmt FROM sqlStatement;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `DynamicDelete` (IN `tableName` VARCHAR(255), IN `whereCondition` TEXT, IN `orderBy` TEXT, IN `groupBy` TEXT, IN `havingCondition` TEXT)   BEGIN
    DECLARE sqlStatement TEXT;  -- Declaración SQL para construir la consulta
    DECLARE errMsg TEXT;        -- Mensaje de error

    -- Validar que la tabla existe
    IF (SELECT COUNT(*) FROM information_schema.tables 
        WHERE table_name = tableName AND table_schema = DATABASE()) = 0 THEN
        SET errMsg = CONCAT('La tabla "', tableName, '" no existe.');
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = errMsg;
    END IF;

    -- Construir la sentencia SQL DELETE
    SET sqlStatement = CONCAT('DELETE FROM ', tableName);

    -- Agregar WHERE si existe
    IF whereCondition IS NOT NULL AND whereCondition != '' THEN
        SET sqlStatement = CONCAT(sqlStatement, ' WHERE ', whereCondition);
    END IF;

    -- Agregar GROUP BY si existe
    IF groupBy IS NOT NULL AND groupBy != '' THEN
        SET sqlStatement = CONCAT(sqlStatement, ' GROUP BY ', groupBy);
    END IF;

    -- Agregar HAVING si existe
    IF havingCondition IS NOT NULL AND havingCondition != '' THEN
        SET sqlStatement = CONCAT(sqlStatement, ' HAVING ', havingCondition);
    END IF;

    -- Agregar ORDER BY si existe
    IF orderBy IS NOT NULL AND orderBy != '' THEN
        SET sqlStatement = CONCAT(sqlStatement, ' ORDER BY ', orderBy);
    END IF;

    -- Preparar y ejecutar la consulta dinámica
    PREPARE stmt FROM sqlStatement;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    -- Mensaje de éxito
    SELECT CONCAT('Consulta ejecutada: ', sqlStatement) AS Query_Executed;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `DynamicInsert` (IN `tableName` VARCHAR(255), IN `jsonData` JSON)   BEGIN
    DECLARE sqlStatement TEXT;
    DECLARE columns TEXT;
    DECLARE valueList TEXT;  -- Cambié el nombre de la variable
    DECLARE errMsg TEXT;

    -- Validar que la tabla existe
    IF (SELECT COUNT(*) FROM information_schema.tables 
        WHERE table_name = tableName AND table_schema = DATABASE()) = 0 THEN
        SET errMsg = CONCAT('La tabla "', tableName, '" no existe.');
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = errMsg;
    END IF;

    -- Construir la lista de columnas
    SET columns = (SELECT GROUP_CONCAT(column_name SEPARATOR ', ')
                   FROM information_schema.columns
                   WHERE table_name = tableName AND table_schema = DATABASE());

    -- Validar que se hayan obtenido columnas
    IF columns IS NULL THEN
        SET errMsg = CONCAT('No se encontraron columnas en la tabla "', tableName, '".');
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = errMsg;
    END IF;

    -- Construir la lista de valores usando los datos del JSON
    SET valueList = (SELECT GROUP_CONCAT(
                        CASE 
                            WHEN JSON_UNQUOTE(JSON_EXTRACT(jsonData, CONCAT('$.', column_name))) IS NULL THEN 'NULL'
                            ELSE CONCAT('"', JSON_UNQUOTE(JSON_EXTRACT(jsonData, CONCAT('$.', column_name))), '"')
                        END
                        SEPARATOR ', ')
                    FROM information_schema.columns
                    WHERE table_name = tableName AND table_schema = DATABASE());

    -- Validar que se hayan obtenido valores
    IF valueList IS NULL OR valueList = '' THEN
        SET errMsg = 'No se proporcionaron valores válidos para el INSERT.';
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = errMsg;
    END IF;

    -- Crear la sentencia SQL dinámica
    SET sqlStatement = CONCAT('INSERT INTO ', tableName, ' (', columns, ') VALUES (', valueList, ')');

    -- Preparar y ejecutar la declaración
    PREPARE stmt FROM sqlStatement;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividad`
--

CREATE TABLE `actividad` (
  `ID_Actividad` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Tipo` varchar(255) DEFAULT NULL COMMENT 'Educativa, Recreativa, Laboral',
  `Horario` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `celda`
--

CREATE TABLE `celda` (
  `ID_Celda` int(11) NOT NULL,
  `Ubicacion` varchar(255) DEFAULT NULL,
  `Capacidad` int(11) DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL COMMENT 'Ocupada, Disponible'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `celda`
--

INSERT INTO `celda` (`ID_Celda`, `Ubicacion`, `Capacidad`, `Estado`) VALUES
(1, 'Medellin2', NULL, NULL),
(2, 'Medellin2', 5, 'Disponible'),
(3, 'Bello', 10, 'Disponible'),
(4, 'Aranjuez', 100, 'Disponible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `condena`
--

CREATE TABLE `condena` (
  `ID_Condena` int(11) NOT NULL,
  `ID_Interno` int(11) DEFAULT NULL,
  `ID_Delito` int(11) DEFAULT NULL,
  `Fecha_Inicio` date DEFAULT NULL,
  `Duracion` int(11) DEFAULT NULL COMMENT 'En meses',
  `Tipo` varchar(255) DEFAULT NULL COMMENT 'Ejemplo: Permanente, Temporal',
  `ID_Personal` int(11) DEFAULT NULL COMMENT 'Responsable de la condena'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `delito`
--

CREATE TABLE `delito` (
  `ID_Delito` int(11) NOT NULL,
  `Tipo` varchar(255) DEFAULT NULL,
  `Descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `delito`
--

INSERT INTO `delito` (`ID_Delito`, `Tipo`, `Descripcion`) VALUES
(1, 'Mano armada', 'Puñalada en un ojo'),
(2, 'asesinato', 'fleteo'),
(3, 'corrupcion', 'abogado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informe_disciplina`
--

CREATE TABLE `informe_disciplina` (
  `ID_Informe` int(11) NOT NULL,
  `ID_Interno` int(11) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Descripcion` text DEFAULT NULL,
  `Sancion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `interno`
--

CREATE TABLE `interno` (
  `ID_Interno` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Fecha_Ingreso` date DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL COMMENT 'Activo, Liberado, Transferido',
  `ID_Celda` int(11) DEFAULT NULL,
  `Fecha_Liberacion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `interno_actividad`
--

CREATE TABLE `interno_actividad` (
  `ID_Interno` int(11) NOT NULL,
  `ID_Actividad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal`
--

CREATE TABLE `personal` (
  `ID_Personal` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Rol` varchar(255) DEFAULT NULL COMMENT 'Ejemplo: Guardia, Administrador',
  `Horario` varchar(255) DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL COMMENT 'Activo, Inactivo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transferencia`
--

CREATE TABLE `transferencia` (
  `ID_Transferencia` int(11) NOT NULL,
  `ID_Interno` int(11) DEFAULT NULL,
  `ID_Celda_Origen` int(11) DEFAULT NULL,
  `ID_Celda_Destino` int(11) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Motivo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visita`
--

CREATE TABLE `visita` (
  `ID_Visita` int(11) NOT NULL,
  `ID_Interno` int(11) DEFAULT NULL,
  `ID_Visitante` int(11) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `Hora_Inicio` time DEFAULT NULL,
  `Duracion` int(11) DEFAULT NULL COMMENT 'En minutos'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitante`
--

CREATE TABLE `visitante` (
  `ID_Visitante` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Relacion` varchar(255) DEFAULT NULL COMMENT 'Ejemplo: Familiar, Abogado',
  `Documento` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visita_multiple`
--

CREATE TABLE `visita_multiple` (
  `ID_Visita` int(11) NOT NULL,
  `ID_Visitante` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD PRIMARY KEY (`ID_Actividad`);

--
-- Indices de la tabla `celda`
--
ALTER TABLE `celda`
  ADD PRIMARY KEY (`ID_Celda`);

--
-- Indices de la tabla `condena`
--
ALTER TABLE `condena`
  ADD PRIMARY KEY (`ID_Condena`),
  ADD KEY `ID_Interno` (`ID_Interno`),
  ADD KEY `ID_Delito` (`ID_Delito`),
  ADD KEY `ID_Personal` (`ID_Personal`);

--
-- Indices de la tabla `delito`
--
ALTER TABLE `delito`
  ADD PRIMARY KEY (`ID_Delito`);

--
-- Indices de la tabla `informe_disciplina`
--
ALTER TABLE `informe_disciplina`
  ADD PRIMARY KEY (`ID_Informe`),
  ADD KEY `ID_Interno` (`ID_Interno`);

--
-- Indices de la tabla `interno`
--
ALTER TABLE `interno`
  ADD PRIMARY KEY (`ID_Interno`),
  ADD KEY `ID_Celda` (`ID_Celda`);

--
-- Indices de la tabla `interno_actividad`
--
ALTER TABLE `interno_actividad`
  ADD PRIMARY KEY (`ID_Interno`,`ID_Actividad`),
  ADD KEY `ID_Actividad` (`ID_Actividad`);

--
-- Indices de la tabla `personal`
--
ALTER TABLE `personal`
  ADD PRIMARY KEY (`ID_Personal`);

--
-- Indices de la tabla `transferencia`
--
ALTER TABLE `transferencia`
  ADD PRIMARY KEY (`ID_Transferencia`),
  ADD KEY `ID_Interno` (`ID_Interno`),
  ADD KEY `ID_Celda_Origen` (`ID_Celda_Origen`),
  ADD KEY `ID_Celda_Destino` (`ID_Celda_Destino`);

--
-- Indices de la tabla `visita`
--
ALTER TABLE `visita`
  ADD PRIMARY KEY (`ID_Visita`),
  ADD KEY `ID_Interno` (`ID_Interno`),
  ADD KEY `ID_Visitante` (`ID_Visitante`);

--
-- Indices de la tabla `visitante`
--
ALTER TABLE `visitante`
  ADD PRIMARY KEY (`ID_Visitante`);

--
-- Indices de la tabla `visita_multiple`
--
ALTER TABLE `visita_multiple`
  ADD PRIMARY KEY (`ID_Visita`,`ID_Visitante`),
  ADD KEY `ID_Visitante` (`ID_Visitante`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `condena`
--
ALTER TABLE `condena`
  ADD CONSTRAINT `condena_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID_Interno`),
  ADD CONSTRAINT `condena_ibfk_2` FOREIGN KEY (`ID_Delito`) REFERENCES `delito` (`ID_Delito`),
  ADD CONSTRAINT `condena_ibfk_3` FOREIGN KEY (`ID_Personal`) REFERENCES `personal` (`ID_Personal`);

--
-- Filtros para la tabla `informe_disciplina`
--
ALTER TABLE `informe_disciplina`
  ADD CONSTRAINT `informe_disciplina_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID_Interno`);

--
-- Filtros para la tabla `interno`
--
ALTER TABLE `interno`
  ADD CONSTRAINT `interno_ibfk_1` FOREIGN KEY (`ID_Celda`) REFERENCES `celda` (`ID_Celda`);

--
-- Filtros para la tabla `interno_actividad`
--
ALTER TABLE `interno_actividad`
  ADD CONSTRAINT `interno_actividad_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID_Interno`),
  ADD CONSTRAINT `interno_actividad_ibfk_2` FOREIGN KEY (`ID_Actividad`) REFERENCES `actividad` (`ID_Actividad`);

--
-- Filtros para la tabla `transferencia`
--
ALTER TABLE `transferencia`
  ADD CONSTRAINT `transferencia_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID_Interno`),
  ADD CONSTRAINT `transferencia_ibfk_2` FOREIGN KEY (`ID_Celda_Origen`) REFERENCES `celda` (`ID_Celda`),
  ADD CONSTRAINT `transferencia_ibfk_3` FOREIGN KEY (`ID_Celda_Destino`) REFERENCES `celda` (`ID_Celda`);

--
-- Filtros para la tabla `visita`
--
ALTER TABLE `visita`
  ADD CONSTRAINT `visita_ibfk_1` FOREIGN KEY (`ID_Interno`) REFERENCES `interno` (`ID_Interno`),
  ADD CONSTRAINT `visita_ibfk_2` FOREIGN KEY (`ID_Visitante`) REFERENCES `visitante` (`ID_Visitante`);

--
-- Filtros para la tabla `visita_multiple`
--
ALTER TABLE `visita_multiple`
  ADD CONSTRAINT `visita_multiple_ibfk_1` FOREIGN KEY (`ID_Visita`) REFERENCES `visita` (`ID_Visita`),
  ADD CONSTRAINT `visita_multiple_ibfk_2` FOREIGN KEY (`ID_Visitante`) REFERENCES `visitante` (`ID_Visitante`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
