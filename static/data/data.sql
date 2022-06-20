create database if not exists school ;

use school;

--  creation de la table user administration 

create table userAdmin(
    id_admin tinyint auto_increment primary key,
    username_admin varchar(50),
    email_admin varchar(255),
    password_admin varchar(255)
);

-- create table parents 

create table 