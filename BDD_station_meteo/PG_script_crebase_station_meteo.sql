/*==============================================================*/
/* Nom de SGBD :  PostgreSQL 8                                  */
/* Date de création :  11/02/2021 15:48:18                      */
/*==============================================================*/

/*
drop index EMET_FK;

drop index T_RELEVE_PK;

drop table T_RELEVE;

drop index T_SONDE_PK;

drop table T_SONDE;
*/
/*==============================================================*/
/* Table : T_RELEVE                                             */
/*==============================================================*/
create table T_RELEVE (
   RELID                SERIAL               not null,
   SONID                INT4                 not null,
   RELDATETIME          DATE                 null,
   RELHUMIDITY          DOUBLE PRECISION              null,
   RELTEMPERATURE       DOUBLE PRECISION              null,
   constraint PK_T_RELEVE primary key (RELID)
);

/*==============================================================*/
/* Index : T_RELEVE_PK                                          */
/*==============================================================*/
create unique index T_RELEVE_PK on T_RELEVE (
RELID
);

/*==============================================================*/
/* Index : EMET_FK                                              */
/*==============================================================*/
create  index EMET_FK on T_RELEVE (
SONID
);

/*==============================================================*/
/* Table : T_SONDE                                              */
/*==============================================================*/
create table T_SONDE (
   SONID                SERIAL               not null,
   SONNAME              VARCHAR(45)          null,
   SONIP                VARCHAR(15)          null,
   SONLOCALISATION      VARCHAR(45)          null,
   SONPROPRIETAIRE      VARCHAR(45)          null,
   constraint PK_T_SONDE primary key (SONID)
);

/*==============================================================*/
/* Index : T_SONDE_PK                                           */
/*==============================================================*/
create unique index T_SONDE_PK on T_SONDE (
SONID
);



