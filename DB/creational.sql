create table [user]
(
    id_card     int         not null,
    id_user     int identity
        constraint user_pk
            primary key nonclustered,
    [name]      varchar(30) not null,
    last_name   varchar(30) not null,
    phoneNumber int         not null,
    email       varchar(100)
)
go

create unique index user_id_card_uindex
    on [user] (id_card)
go

create unique index user_id_user_uindex
    on [user] (id_user)
go
