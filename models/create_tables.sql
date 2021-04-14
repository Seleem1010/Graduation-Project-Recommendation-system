CREATE TABLE IF NOT EXISTS users (id BIGINT PRIMARY KEY NOT NULL, firstname VARCHAR(255) NOT NULL, lastname VARCHAR(255) NOT NULL, email VARCHAR(255) UNIQUE KEY NOT NULL, password VARCHAR(255) NOT NULL, verified INT NOT NULL, reset_code INT NOT NULL DEFAULT 0, image VARCHAR(255) NOT NULL DEFAULT "user.png");

CREATE TABLE IF NOT EXISTS products (id BIGINT PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL, description TEXT NOT NULL, image VARCHAR(255) NOT NULL DEFAULT "product.png", tags VARCHAR(255) NOT NULL DEFAULT "");

CREATE TABLE IF NOT EXISTS favorites (id BIGINT PRIMARY KEY NOT NULL, pid BIGINT NOT NULL, FOREIGN KEY (pid) REFERENCES products (id), uid BIGINT NOT NULL, FOREIGN KEY (uid) REFERENCES users (id), UNIQUE KEY (pid, uid));

CREATE TABLE IF NOT EXISTS comments (id BIGINT PRIMARY KEY NOT NULL, text TEXT NOT NULL, time DATETIME NOT NULL, pid BIGINT NOT NULL, FOREIGN KEY (pid) REFERENCES products (id), uid BIGINT NOT NULL, FOREIGN KEY (uid) REFERENCES users (id), sentiment_analysis BOOLEAN NOT NULL);

CREATE TABLE IF NOT EXISTS ratings (id BIGINT PRIMARY KEY NOT NULL, rate TINYINT NOT NULL, pid BIGINT NOT NULL, FOREIGN KEY (pid) REFERENCES products (id), uid BIGINT NOT NULL, FOREIGN KEY (uid) REFERENCES users (id), UNIQUE KEY (pid, uid));