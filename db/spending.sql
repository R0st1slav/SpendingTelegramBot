create table User(
    chat_id integer not null unique,
    name text
);

create table expense(
    idExp integer primary key autoincrement,
    amount integer not null,
    idCatExp integer,
    FOREIGN KEY(idCatExp) REFERENCES categoryExp(idCatExp)
);

create table incomes(
    idInc integer primary key autoincrement,
    amount integer not null,
    idCatInc integer,
    FOREIGN KEY(idCatInc) REFERENCES categoryInc(idCatInc)
);

create table categoryExp(
    idCatExp integer primary key autoincrement,
    nameCategory text
);

create table categoryInc(
    idCatInc integer primary key autoincrement,
    nameCategory text
);


insert into User values ()
