BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "UnidadeMedida" (
	"un"	char(4) NOT NULL,
	"dsmedida"	varchar(20),
	PRIMARY KEY("un")
);
INSERT INTO "UnidadeMedida" VALUES ('UN','unidade');
INSERT INTO "UnidadeMedida" VALUES ('PCA','pedaço');
INSERT INTO "UnidadeMedida" VALUES ('LT','litro');
COMMIT;
