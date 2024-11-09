-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-11-2024 a las 02:05:19
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
CREATE DEFINER=`root`@`localhost` PROCEDURE `ContarReclusosPorCelda` ()   BEGIN
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

CREATE DEFINER=`root`@`localhost` PROCEDURE `ObtenerCondenaPorInternoYDelito` (IN `p_ID_Interno` INT, IN `p_ID_Delito` INT)   BEGIN
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

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteActividad` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM actividad WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteCelda` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM celda WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteCondena` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM condena WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteDelito` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM delito WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteInformeDisciplina` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM informedisciplina WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteInterno` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM interno WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteInternoActividad` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM internoactividad WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeletePersonal` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM personal WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteTransferencia` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM transferencia WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteVisita` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM visita WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteVisitaMultiple` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM visitamultiple WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteVisitante` (IN `p_condition` VARCHAR(255))   BEGIN
    SET @query = CONCAT('DELETE FROM visitante WHERE ', p_condition);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Insertactividad` (IN `p_actividad_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'actividad';  -- Especificamos la tabla 'actividad'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'actividad' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_actividad_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO actividad (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última actividad insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM actividad WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_InsertCelda` (IN `p_celda_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'celda';  -- Especificamos la tabla 'celda'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'celda' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_celda_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO celda (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última celda insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM celda WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Insertcondena` (IN `p_condena_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'condena';  -- Especificamos la tabla 'condena'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'condena' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_condena_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO condena (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última condena insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM condena WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Insertdelito` (IN `p_delito_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'delito';  -- Especificamos la tabla 'delito'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'delito' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_delito_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO delito (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última delito insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM delito WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_InsertinformeDisciplina` (IN `p_informeDisciplina_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'informeDisciplina';  -- Especificamos la tabla 'informeDisciplina'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'informeDisciplina' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_informeDisciplina_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO informeDisciplina (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última informeDisciplina insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM informeDisciplina WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Insertinterno` (IN `p_interno_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'interno';  -- Especificamos la tabla 'interno'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'interno' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_interno_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO interno (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última interno insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM interno WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_InsertinternoActividad` (IN `p_internoActividad_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'internoActividad';  -- Especificamos la tabla 'internoActividad'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'internoActividad' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_internoActividad_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO internoActividad (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última internoActividad insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM internoActividad WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Insertpersonal` (IN `p_personal_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'personal';  -- Especificamos la tabla 'personal'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'personal' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_personal_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO personal (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última personal insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM personal WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Inserttransferencia` (IN `p_transferencia_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'transferencia';  -- Especificamos la tabla 'transferencia'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'transferencia' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_transferencia_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO transferencia (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última transferencia insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM transferencia WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Insertvisita` (IN `p_visita_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'visita';  -- Especificamos la tabla 'visita'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'visita' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_visita_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO visita (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última visita insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM visita WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_InsertvisitaMultiple` (IN `p_visitaMultiple_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'visitaMultiple';  -- Especificamos la tabla 'visitaMultiple'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'visitaMultiple' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_visitaMultiple_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO visitaMultiple (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última visitaMultiple insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM visitaMultiple WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Insertvisitante` (IN `p_visitante_json` JSON)   BEGIN
    DECLARE v_sql_insert VARCHAR(10000);
    DECLARE v_columns VARCHAR(10000);
    DECLARE v_values VARCHAR(10000);
    DECLARE v_column_name VARCHAR(255);
    DECLARE v_column_value JSON;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'visitante';  -- Especificamos la tabla 'visitante'
 
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
 
    -- Inicializar las variables de columnas y valores
    SET v_columns = '';
    SET v_values = '';
 
    OPEN cur;
 
    -- Recorrer las columnas de la tabla 'visitante' y construir la sentencia SQL
    read_loop: LOOP
        FETCH cur INTO v_column_name;
 
        IF done THEN
            LEAVE read_loop;
        END IF;
 
        -- Obtener el valor del campo correspondiente desde el JSON
        SET v_column_value = JSON_UNQUOTE(JSON_EXTRACT(p_visitante_json, CONCAT('$."', v_column_name, '"')));
 
        -- Verificar si el valor existe en el JSON
        IF v_column_value IS NOT NULL THEN
            -- Si el valor existe, agregarlo a la lista de valores
            IF v_values != '' THEN
                SET v_values = CONCAT(v_values, ', "', v_column_value, '"');
            ELSE
                SET v_values = CONCAT('"', v_column_value, '"');
            END IF;
 
            -- Agregar la columna a la lista de columnas
            IF v_columns != '' THEN
                SET v_columns = CONCAT(v_columns, ', ', v_column_name);
            ELSE
                SET v_columns = v_column_name;
            END IF;
        END IF;
 
    END LOOP;
 
    CLOSE cur;
 
    -- Construir la consulta de inserción
    SET v_sql_insert = CONCAT('INSERT INTO visitante (', v_columns, ') VALUES (', v_values, ')');
 
    -- Ejecutar la consulta dinámica de inserción
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
 
    -- COMMIT para asegurar que la transacción se aplique
    COMMIT;
 
    -- Obtener el ID de la última visitante insertada y devolver la fila
    SET v_sql_insert = 'SELECT * FROM visitante WHERE ID = LAST_INSERT_ID()';
    PREPARE stmt FROM v_sql_insert;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectActividad` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM actividad;
    ELSE
        SELECT * FROM actividad WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectCelda` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        -- Si no se pasa un ID o se pasa un valor que represente "todos"
        SELECT * FROM celda;
    ELSE
        -- Si se pasa un ID válido
        SELECT * FROM celda WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectCondena` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM condena;
    ELSE
        SELECT * FROM condena WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectDelito` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM delito;
    ELSE
        SELECT * FROM delito WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectInformeDisciplina` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM informedisciplina;
    ELSE
        SELECT * FROM informedisciplina WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectInterno` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM interno;
    ELSE
        SELECT * FROM interno WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectInternoActividad` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM internoactividad;
    ELSE
        SELECT * FROM internoactividad WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectPersonal` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM personal;
    ELSE
        SELECT * FROM personal WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectTransferencia` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM transferencia;
    ELSE
        SELECT * FROM transferencia WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectVisita` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM visita;
    ELSE
        SELECT * FROM visita WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectVisitaMultiple` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM visitamultiple;
    ELSE
        SELECT * FROM visitamultiple WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_SelectVisitante` (IN `p_id` INT)   BEGIN
    IF p_id IS NULL OR p_id = 0 THEN
        SELECT * FROM visitante;
    ELSE
        SELECT * FROM visitante WHERE ID = p_id;
    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateActividad` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;
    
    START TRANSACTION;
    
    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'actividad' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE actividad SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM actividad WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;
    
    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_Updatecelda` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
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

    -- Construir la cláusula SET dinámicamente usando el JSON de entrada
    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(
                COLUMN_NAME, ' = ',
                QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))
            ) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'celda'
          AND COLUMN_NAME != 'ID'  -- Excluir el campo ID
    );

    -- Construir la consulta de actualización con el WHERE usando p_Id
    SET @update_sql = CONCAT('UPDATE celda SET ', @set_clause, ' WHERE ID = ', p_Id);
    
    -- Ejecutar la consulta de actualización
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
        SET @result_sql = CONCAT('SELECT * FROM celda WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateCondena` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'condena' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE condena SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM condena WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;
    
    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateDelito` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'delito' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE delito SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM delito WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateInformeDisciplina` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'informedisciplina' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE informedisciplina SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM informedisciplina WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateInterno` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'interno' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE interno SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM interno WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateInternoActividad` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'internoactividad' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE internoactividad SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM internoactividad WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdatePersonal` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'personal' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE personal SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM personal WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateTransferencia` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'transferencia' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE transferencia SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM transferencia WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateVisita` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'visita' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE visita SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM visita WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateVisitaMultiple` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'visitamultiple' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE visitamultiple SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM visitamultiple WHERE ID = ', p_Id);
        PREPARE stmt_result FROM @result_sql;
        EXECUTE stmt_result;
        DEALLOCATE PREPARE stmt_result;
    END IF;

    DEALLOCATE PREPARE stmt_update;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateVisitante` (IN `p_UpdateJSON` JSON, IN `p_Id` INT)   BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al ejecutar la actualización.';
    END;

    START TRANSACTION;

    SET @set_clause = (
        SELECT GROUP_CONCAT(
            CONCAT(COLUMN_NAME, ' = ', QUOTE(JSON_UNQUOTE(JSON_EXTRACT(p_UpdateJSON, CONCAT('$.', COLUMN_NAME))))) SEPARATOR ', '
        )
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'visitante' AND COLUMN_NAME != 'ID'
    );

    SET @update_sql = CONCAT('UPDATE visitante SET ', @set_clause, ' WHERE ID = ', p_Id);
    PREPARE stmt_update FROM @update_sql;
    EXECUTE stmt_update;

    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se realizó ninguna actualización.';
    ELSE
        COMMIT;
        SET @result_sql = CONCAT('SELECT * FROM visitante WHERE ID = ', p_Id);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `celda`
--

CREATE TABLE `celda` (
  `ID` int(11) NOT NULL,
  `Ubicacion` varchar(255) DEFAULT NULL,
  `Capacidad` int(11) DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL COMMENT 'Ocupada, Disponible'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `delito`
--

CREATE TABLE `delito` (
  `ID` int(11) NOT NULL,
  `Tipo` varchar(255) DEFAULT NULL,
  `Descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `internoactividad`
--

CREATE TABLE `internoactividad` (
  `ID` int(11) NOT NULL,
  `ID_Interno` int(11) NOT NULL,
  `ID_Actividad` int(11) NOT NULL,
  `Fecha_Actividad` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitamultiple`
--

CREATE TABLE `visitamultiple` (
  `ID` int(11) NOT NULL,
  `ID_Visita` int(11) NOT NULL,
  `ID_Visitante` int(11) NOT NULL,
  `Observacion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitante`
--

CREATE TABLE `visitante` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Relacion` varchar(255) DEFAULT NULL COMMENT 'Ejemplo: Familiar, Abogado',
  `Documento` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `celda`
--
ALTER TABLE `celda`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `condena`
--
ALTER TABLE `condena`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `delito`
--
ALTER TABLE `delito`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `informedisciplina`
--
ALTER TABLE `informedisciplina`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `interno`
--
ALTER TABLE `interno`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `internoactividad`
--
ALTER TABLE `internoactividad`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `personal`
--
ALTER TABLE `personal`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `transferencia`
--
ALTER TABLE `transferencia`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `visita`
--
ALTER TABLE `visita`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `visitamultiple`
--
ALTER TABLE `visitamultiple`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `visitante`
--
ALTER TABLE `visitante`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
