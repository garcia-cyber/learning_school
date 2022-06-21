create database if not exists school ;

use school;

--  creation de la table user administration 

create table userAdmin(
    id_admin tinyint auto_increment primary key,
    username_admin varchar(50),
    email_admin varchar(100),
    password_admin varchar(255)
);

-- ajout du user et password par defaut

insert into userAdmin(username_admin,email_admin,password_admin)values('mukoko','mukokogarciagx@gmail.com','user');



-- table commune 
create table communes(
    id_commune tinyint auto_increment primary key,
    lib_commune varchar(25)
);

-- insertion de quelques communes 

insert into communes(lib_commune)values("Matete"),("Limete"),("Lemba"),("N'djili")("Masina");

-- create table parents  avec commune comme cle etranger

create table parents(
    id_parent smallint auto_increment primary key,
    username_parent varchar(50),
    email_parent varchar(100),
    commune_parent tinyint,
    adresse_parent varchar(150),
    phone_parent varchar(15),
    password_parent varchar(255)
);






-- add foreign key with all setting
alter table parents add constraint fk_commune foreign key(commune_parent) references communes(id_commune)
on delete set null  on update cascade;



