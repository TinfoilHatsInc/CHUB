BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Type` (
	`ID`	INTEGER NOT NULL UNIQUE,
	`Name`	INTEGER NOT NULL,
	PRIMARY KEY(`ID`)
);
CREATE TABLE IF NOT EXISTS `Room` (
	`ID`	INTEGER NOT NULL UNIQUE,
	`Name`	TEXT NOT NULL,
	PRIMARY KEY(`ID`)
);
CREATE TABLE IF NOT EXISTS `Recording` (
	`ID`	INTEGER NOT NULL UNIQUE,
	`Event`	INTEGER NOT NULL,
	`File_Location`	TEXT NOT NULL,
	PRIMARY KEY(`ID`)
);
CREATE TABLE IF NOT EXISTS `Module` (
	`ID`	INTEGER NOT NULL UNIQUE,
	`Name`	TEXT NOT NULL,
	`Type`	INTEGER NOT NULL,
	`Room`	INTEGER NOT NULL,
	`Alive`	INTEGER NOT NULL,
	PRIMARY KEY(`ID`)
);
CREATE TABLE IF NOT EXISTS `Event` (
	`ID`	INTEGER NOT NULL UNIQUE,
	`Room`	INTEGER NOT NULL,
	`Date_Time`	TEXT NOT NULL,
	PRIMARY KEY(`ID`)
);
CREATE TABLE IF NOT EXISTS `ConfigurationOverrides` (
	`Module`	INTEGER NOT NULL UNIQUE,
	`Name`	TEXT NOT NULL,
	`Value`	INTEGER,
	PRIMARY KEY(`Module`,`Name`)
);
COMMIT;