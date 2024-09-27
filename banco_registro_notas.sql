--
-- File generated with SQLiteStudio v3.4.4 on sex set 27 14:47:57 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: tb_alunos
CREATE TABLE IF NOT EXISTS tb_alunos (matricula INTEGER PRIMARY KEY, nome TEXT, curso TEXT, "");
INSERT INTO tb_alunos (matricula, nome, curso, "") VALUES (123, 'ramalho', 'direito', NULL);
INSERT INTO tb_alunos (matricula, nome, curso, "") VALUES (1552, 'João mariano', 'ciencia da computacao', NULL);
INSERT INTO tb_alunos (matricula, nome, curso, "") VALUES (1553, 'Juliana', 'ciencia da computacao', NULL);
INSERT INTO tb_alunos (matricula, nome, curso, "") VALUES (555555, 'mario lago', 'ciencia de dados', NULL);
INSERT INTO tb_alunos (matricula, nome, curso, "") VALUES (22222222, 'rodrigo', 'analise e desenvolvimento de sistemas', NULL);

-- Table: tb_notas
CREATE TABLE IF NOT EXISTS tb_notas (item INTEGER PRIMARY KEY, valor REAL, matricula INTEGER REFERENCES tb_alunos (matricula));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
