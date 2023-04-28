create database telecomunicações;
use telecomunicações;

create table cliente (
		codigocliente int auto_increment primary key,
        cpfcliente varchar (15),
        nomecliente varchar (70),
        datanascimentocliente datetime,
        enderecocliente varchar (60),
        cepcliente varchar (12),
        bairrocliente varchar (30),
        cidadecliente varchar (40),
        ufcliente varchar (2)
        );
        
alter table cliente add dataultimacompracliente datetime;

insert into cliente (
		cpfcliente,
        nomecliente,
        datanascimentocliente,
        enderecocliente,
        cepcliente,
        bairrocliente,
        cidadecliente,
        ufcliente
		)
        values
        
        ('04496332780', 'João da Silva', '19691125', 'Rua Antônio Numes', '88045963', 'Palmeiras', 'Londrina', 'PR'),
        ('05485031490', 'Ana Regina Fagundes', '19860921', 'Rua Palmeias Novas', '88078923', 'Leblon', 'Rio de Janeiro', 'RJ'),
        ('03350314905', 'Fernando Soares', '19900305', 'Rua Palmeias Novas', '88048917', 'Copacabana', 'Rio de Janeiro', 'RJ');
        
select * from cliente where cidadecliente = 'Rio de Janeiro';
delete from cliente where cidadecliente = 'Londrina';