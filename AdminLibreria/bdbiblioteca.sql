-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-07-2023 a las 19:44:47
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdbiblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--

CREATE TABLE `autor` (
  `ID_AUTOR` int(9) NOT NULL,
  `NOMBRE_AUTOR` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_autor`
--

CREATE TABLE `detalle_autor` (
  `ID_DETALLE_AUTOR` int(9) NOT NULL,
  `ID_AUTOR` int(9) NOT NULL,
  `ID_LIBRO` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_prestamo`
--

CREATE TABLE `detalle_prestamo` (
  `ID_DETALLE` int(9) NOT NULL,
  `ID_PRESTAMO` int(9) NOT NULL,
  `ID_LIBRO` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `ID_LIBRO` int(9) NOT NULL,
  `EDITORIAL` varchar(20) NOT NULL,
  `NOMBRE_LIBRO` varchar(30) NOT NULL,
  `ESTADO_LIBRO` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `libro`
--

INSERT INTO `libro` (`ID_LIBRO`, `EDITORIAL`, `NOMBRE_LIBRO`, `ESTADO_LIBRO`) VALUES
(3, 'Hola mundo', 'Intenautas', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo`
--

CREATE TABLE `prestamo` (
  `ID_PRESTAMO` int(9) NOT NULL,
  `FECHA_PRESTAMO` date NOT NULL,
  `FECHA_DEVOLUCION` date NOT NULL,
  `RENOVACION` date DEFAULT NULL,
  `RUT` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `RUT` varchar(13) NOT NULL,
  `NOMBRE` varchar(40) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `DIRECCION` varchar(50) NOT NULL,
  `TELEFONO` varchar(15) NOT NULL,
  `TIPO_USUARIO` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`RUT`, `NOMBRE`, `EMAIL`, `DIRECCION`, `TELEFONO`, `TIPO_USUARIO`) VALUES
('111-1', 'Pablo', 'pablitoxl@mail', 'Avenida libertador 99', '999999999', 'Alumno'),
('20004235-2', 'Chris', 'chris@mail', 'Kalilas 99', '999987766', 'Bibliotecario'),
('222-2', 'Cesar', 'ceraritox@mail.com', 'Escuela agricola 1', '988887777', 'Docente');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`ID_AUTOR`);

--
-- Indices de la tabla `detalle_autor`
--
ALTER TABLE `detalle_autor`
  ADD PRIMARY KEY (`ID_DETALLE_AUTOR`),
  ADD KEY `ID_AUTOR` (`ID_AUTOR`),
  ADD KEY `ID_LIBRO` (`ID_LIBRO`);

--
-- Indices de la tabla `detalle_prestamo`
--
ALTER TABLE `detalle_prestamo`
  ADD PRIMARY KEY (`ID_DETALLE`),
  ADD KEY `ID_PRESTAMO` (`ID_PRESTAMO`),
  ADD KEY `ID_LIBRO` (`ID_LIBRO`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`ID_LIBRO`);

--
-- Indices de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD PRIMARY KEY (`ID_PRESTAMO`),
  ADD KEY `RUT` (`RUT`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`RUT`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autor`
--
ALTER TABLE `autor`
  MODIFY `ID_AUTOR` int(9) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_autor`
--
ALTER TABLE `detalle_autor`
  MODIFY `ID_DETALLE_AUTOR` int(9) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_prestamo`
--
ALTER TABLE `detalle_prestamo`
  MODIFY `ID_DETALLE` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `libro`
--
ALTER TABLE `libro`
  MODIFY `ID_LIBRO` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  MODIFY `ID_PRESTAMO` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `detalle_autor`
--
ALTER TABLE `detalle_autor`
  ADD CONSTRAINT `detalle_autor_ibfk_1` FOREIGN KEY (`ID_AUTOR`) REFERENCES `autor` (`ID_AUTOR`),
  ADD CONSTRAINT `detalle_autor_ibfk_2` FOREIGN KEY (`ID_LIBRO`) REFERENCES `libro` (`ID_LIBRO`);

--
-- Filtros para la tabla `detalle_prestamo`
--
ALTER TABLE `detalle_prestamo`
  ADD CONSTRAINT `detalle_prestamo_ibfk_1` FOREIGN KEY (`ID_PRESTAMO`) REFERENCES `prestamo` (`ID_PRESTAMO`),
  ADD CONSTRAINT `detalle_prestamo_ibfk_2` FOREIGN KEY (`ID_LIBRO`) REFERENCES `libro` (`ID_LIBRO`);

--
-- Filtros para la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD CONSTRAINT `prestamo_ibfk_1` FOREIGN KEY (`RUT`) REFERENCES `usuario` (`RUT`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
