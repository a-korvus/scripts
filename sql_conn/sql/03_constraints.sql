-- Ограничения внешнего ключа таблицы "good";
ALTER TABLE "good"
  ADD CONSTRAINT "good_category_fk" FOREIGN KEY ("category_id") REFERENCES "good_category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- Ограничения внешнего ключа таблицы "good_category";
ALTER TABLE "good_category"
  ADD CONSTRAINT "parent_category_fk" FOREIGN KEY ("parent_id") REFERENCES "good_category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- Ограничения внешнего ключа таблицы "order";
ALTER TABLE "order"
  ADD CONSTRAINT "user_fk" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT "status_fk" FOREIGN KEY ("status_id") REFERENCES "order_status" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- Ограничения внешнего ключа таблицы "order2good";
ALTER TABLE "order2good"
  ADD CONSTRAINT "order_fk" FOREIGN KEY ("order_id") REFERENCES "order" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT "good_fk" FOREIGN KEY ("good_id") REFERENCES "good" ("id") ON DELETE CASCADE ON UPDATE NO ACTION;

-- Ограничения внешнего ключа таблицы "order_status_change";
ALTER TABLE "order_status_change"
  ADD CONSTRAINT "order_fk" FOREIGN KEY ("order_id") REFERENCES "order" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT "src_status_fk" FOREIGN KEY ("src_status_id") REFERENCES "order_status" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT "dst_status_fk" FOREIGN KEY ("dst_status_id") REFERENCES "order_status" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
