CREATE TABLE Membro(
	id INT AUTO_INCREMENT,
    email VARCHAR(50) NOT NULL UNIQUE,
    nome VARCHAR(50) NOT NULL,
	PRIMARY KEY (id),
    CONSTRAINT tamanho_minimo_nome CHECK (CHAR_LENGTH(nome) >= 5)
);

CREATE TABLE Tarefa(
	id INT AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(140),
    finalizada BOOLEAN NOT NULL,
    data_termino DATE,
    prioridade ENUM('Baixa', 'Média', 'Alta') DEFAULT 'Baixa',
	criador_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (criador_id) REFERENCES membro(id),
	CONSTRAINT tamanho_minimo_nome_tarefa CHECK (CHAR_LENGTH(nome) >= 5)

);