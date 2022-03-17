drop table if exists cryptocurrencys;

create table cryptocurrencys(
    cryptocurrency_id int auto_increment,
    cryptocurrency_name varchar(100) not null,
    cryptocurrency_symbol varchar(10),
    created_at timestamp default current_timestamp,
    primary key(cryptocurrency_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO cryptocurrencys (cryptocurrency_name, cryptocurrency_symbol) VALUES ('Bitcoin', 'BTC');
INSERT INTO cryptocurrencys (cryptocurrency_name, cryptocurrency_symbol) VALUES ('Theter', 'USDT');
INSERT INTO cryptocurrencys (cryptocurrency_name, cryptocurrency_symbol) VALUES ('Ethereum', 'ETH');
INSERT INTO cryptocurrencys (cryptocurrency_name, cryptocurrency_symbol) VALUES ('Dogecoin', 'DOGE');
INSERT INTO cryptocurrencys (cryptocurrency_name, cryptocurrency_symbol) VALUES ('Rafacoin', 'RAFA');
INSERT INTO cryptocurrencys (cryptocurrency_name, cryptocurrency_symbol) VALUES ('Binancecoin', 'BNC');