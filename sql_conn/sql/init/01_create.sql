-- Структура таблицы "good";
CREATE TABLE "good" (
  id serial PRIMARY KEY,
  category_id integer NOT NULL,
  name character varying(255),
  count integer NOT NULL,
  price integer NOT NULL
);

-- Структура таблицы "good_category";
CREATE TABLE "good_category" (
  id serial PRIMARY KEY,
  parent_id integer,
  name character varying(255) NOT NULL
);

-- Структура таблицы "order";
CREATE TABLE "order" (
  id serial PRIMARY KEY,
  user_id integer NOT NULL,
  status_id integer NOT NULL,
  creation_date timestamp without time zone NOT NULL
);

-- Структура таблицы "order2good";
CREATE TABLE "order2good" (
  order_id integer NOT NULL,
  good_id integer NOT NULL,
  count integer NOT NULL,
  PRIMARY KEY (order_id, good_id)
);

-- Структура таблицы "order_status";
CREATE TABLE "order_status" (
  id serial PRIMARY KEY,
  sort_index integer NOT NULL,
  code character varying(255) NOT NULL,
  name character varying(255) NOT NULL
);

-- Структура таблицы "order_status_change";
CREATE TABLE "order_status_change" (
  id serial PRIMARY KEY,
  order_id integer NOT NULL,
  time timestamp without time zone NOT NULL,
  src_status_id integer NOT NULL,
  dst_status_id integer NOT NULL
);

-- Структура таблицы "user";
CREATE TABLE "user" (
  id serial PRIMARY KEY,
  name character varying(255) NOT NULL,
  email character varying(255) NOT NULL,
  password character varying(255) NOT NULL,
  reg_date timestamp without time zone NOT NULL
);

-- Индексы таблицы "good";
CREATE INDEX category_id_idx ON "good" (category_id);

-- Индексы таблицы "good_category";
CREATE INDEX parent_id_idx ON "good_category" (parent_id);

-- Индексы таблицы "order";
CREATE INDEX user_id_idx ON "order" (user_id);
CREATE INDEX status_id_idx ON "order" (status_id);

-- Индексы таблицы "order2good";
CREATE INDEX good_id_idx ON "order2good" (good_id);

-- Индексы таблицы "order_status_change";
CREATE INDEX order_id_idx ON "order_status_change" (order_id);
CREATE INDEX src_status_id_idx ON "order_status_change" (src_status_id);
CREATE INDEX dst_status_id_idx ON "order_status_change" (dst_status_id);