/*==============================================================*/
/* Nom de SGBD :  PostgreSQL 8                                  */
/* Date de création :  09/02/2021 15:01:46                      */
/*==============================================================*/


drop index EMET_FK;

drop index T_RELEVE_PK;

drop table T_RELEVE;

drop index T_SONDE_PK;

drop table T_SONDE;

drop index ENVOIE_FK;

drop index T_TEMP_REL_PK;

drop table T_TEMP_REL;

/*==============================================================*/
/* Table : T_RELEVE                                             */
/*==============================================================*/
create table T_RELEVE (
   RELID                SERIAL               not null,
   SONID                INT4                 not null,
   RELDATETIME          DATE                 null,
   RELHUMIDITY          DECIMAL(2,2)         null,
   RELTEMPERATURE       DECIMAL(2,2)         null,
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

/*==============================================================*/
/* Table : T_TEMP_REL                                           */
/*==============================================================*/
create table T_TEMP_REL (
   TRELID               SERIAL               not null,
   SONID                INT4                 not null,
   TRELDATETIME         DATE                 null,
   TRELHUMIDITY         DECIMAL(2,2)         null,
   TRELTEMPERATURE      DECIMAL(2,2)         null,
   constraint PK_T_TEMP_REL primary key (TRELID)
);

/*==============================================================*/
/* Index : T_TEMP_REL_PK                                        */
/*==============================================================*/
create unique index T_TEMP_REL_PK on T_TEMP_REL (
TRELID
);

/*==============================================================*/
/* Index : ENVOIE_FK                                            */
/*==============================================================*/
create  index ENVOIE_FK on T_TEMP_REL (
SONID
);

alter table T_RELEVE
   add constraint FK_T_RELEVE_EMET_T_SONDE foreign key (SONID)
      references T_SONDE (SONID)
      on delete restrict on update restrict;

alter table T_TEMP_REL
   add constraint FK_T_TEMP_R_ENVOIE_T_SONDE foreign key (SONID)
      references T_SONDE (SONID)
      on delete restrict on update restrict;

