instructions = [
    "SET FOREIGN_KEY_CHECKS=0",#DESABILITA LAS LLAVES FORANEAS PARA PODER ELEIMINAR LAS TABLAS
    "DROP TABLE IF EXISTS todo",
    "DROP TABLE IF EXISTS user",
    "SET FOREIGN_KEY_CHECKS=1",
    """
    CREATE TABLE user(
        id int PRIMARY KEY AUTO_INCREMENT,
        username varchar(50) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL   
    )     
    """,
    """
    CREATE TABLE todo(
        id int PRIMARY KEY AUTO_INCREMENT,
        created_by int NOT NULL,
        created_at TIMESTAMP  NOT NULL DEFAULT CURRENT_TIMESTAMP,
        completed BOOLEAN NOT NULL,
        FOREIGN KEY (created_by) REFERENCES user(id)  
    )     
    """
    
    
]