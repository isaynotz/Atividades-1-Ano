create database PetShop;
use PetShop;

create table Animal (
    IdA int auto_increment primary key,
    NomeA varchar (40),
    Raca int references Especie(IdE)
);

create table Especie (
    IdE int auto_increment primary key,
    NomeE varchar (50)    
);

create table Dono (
    IdD int auto_increment primary key,
    NomeD varchar (60),
    CPFD varchar (14),
    TelefoneD varchar (12)
);

alter table Animal add constraint foreign key (FK_DonoA) references Dono(IdD);

rename table Especie to Raca;

insert into Animal (
    NomeA,
    Raca,
    FK_DonoA
)

values
    ('Toto','1','2'),
    ('Toto','2','3'),
    ('Lica','1','1'),
    ('Brutus','3','1'),
    ('Pluto','1','1');

insert into Dono (
    NomeD,
    CPFD,
    TelefoneD
)

values
    ('João','1234','3333 4444'),
    ('Pedro','5678','3333 5555'),
    ('José','9123','3333 6666'),
    ('Maria','6523','3333 2222');

insert into Raca (
    NomeE
)

values
    ('Vira-lata'),
    ('Poodle'),
    ('Husky Siberiano');

update Animal
set NomeA = 'Rex'
where IdA = 4;

delete from Animal where IdA = 2;

update Animal
set IdD = 4
where IdA = 3;

create table Consulta(
    IdC int auto_increment primary key,
    DataC datetime,
    Animal int references Animal(IdA)
);

alter table Consulta add Hora time;

insert into Consulta (
    DataC,
    Animal,
    Hora
)

values
    ('20070112','1','07:00'),
    ('20070112','3','08:00'),
    ('20070113','1','07:00');

delete from Consulta where IdC = 1;

update Consulta
set Hora = '20070113'
where IdC = 3;