--
-- File generated with SQLiteStudio v3.4.4 on sex set 27 14:44:43 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: tbcadastro
CREATE TABLE IF NOT EXISTS tbcadastro (codigo INTEGER, nome TEXT, idade INTEGER, cpf INTEGER PRIMARY KEY, rua INTEGER, cep NUMERIC);
INSERT INTO tbcadastro (codigo, nome, idade, cpf, rua, cep) VALUES (1, 'mario', 44, 1, NULL, NULL);
INSERT INTO tbcadastro (codigo, nome, idade, cpf, rua, cep) VALUES (12996, 'margarete pahares', 40, 5533322, 'almirante barroso', 77775545);
INSERT INTO tbcadastro (codigo, nome, idade, cpf, rua, cep) VALUES (12996, 'graldo', 38, 5552522, 'candido benicio', 21885545);
INSERT INTO tbcadastro (codigo, nome, idade, cpf, rua, cep) VALUES (12996, 'graldo', 34, 121212212, 'maracana', 555545544);
INSERT INTO tbcadastro (codigo, nome, idade, cpf, rua, cep) VALUES (1255, 'marcos', 34, 121221212, 'rio branco', 2551034);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
