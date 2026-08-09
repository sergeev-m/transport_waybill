# загружаем .env (удаляем комментарии и пустые строки)
ifneq (,$(wildcard .env))
  include .env
endif
export


### CONFIG ###
MODULE=transport
CONTAINER=transport_odoo
DB_CONTAINER=$(CONTAINER)_db
ADDONS=addons/$(MODULE)/i18n
POFILE=$(ADDONS)/$(LANG).po
POFILE_MOUNTED='/mnt/extra-addons/$(MODULE)/i18n'

DEFAULT_LANG := ru
LANG = $(DEFAULT_LANG)


### COMMON ###

logs:
	docker logs -f $(CONTAINER) --tail 50

exec:
	docker exec -it $(CONTAINER) bash

db-shell:
	docker exec -it $(DB_CONTAINER) psql -U $(POSTGRES_USER) -d $(DB_NAME)
# 	docker exec -it $(DB_CONTAINER) bash -c 'psql -U $$POSTGRES_USER -d $$DB_NAME'

shell:
	docker exec -it $(CONTAINER) odoo shell -d $(DB_NAME)

restart:
	docker compose restart $(CONTAINER)

stop:
	docker compose stop

run:
	docker compose up -d

run-prod:
	docker compose -f docker-compose.yml up -d

rebuild:
	docker compose down
	docker compose up -d --build

### MODULE MANAGEMENT ###

update:
	docker exec $(CONTAINER) odoo -d $(DB_NAME) -u $(MODULE) --stop-after-init

i18n_export:
ifeq ($(LANG),$(DEFAULT_LANG))
	@echo "⚠ Используется язык по умолчанию: $(LANG)"
	@echo "ℹ Чтобы экспортировать другой язык: make i18n_export LANG=en"
endif
	@echo "Exporting translations for the language: $(LANG)"
	docker exec $(CONTAINER) sh -c "odoo i18n export -d $(DB_NAME) -l $(LANG) -o /tmp/export.po $(MODULE)" 
	docker cp $(CONTAINER):/tmp/export.po $(POFILE)
	msgattrib --no-obsolete $(POFILE) -o $(POFILE)
	msgcat --sort-output $(POFILE) -o $(POFILE)
	@echo "✔ Exported to $(POFILE)"

i18n_update:
	@echo "\n📥 Import translations..."
	docker exec $(CONTAINER) bash -c "odoo i18n import -d $(DB_NAME) -l $(LANG) $(POFILE_MOUNTED)/$(LANG).po && \
	odoo i18n loadlang -l $(LANG)"
	
	make update
	@echo "✔ Imported to DB"


### BACKUP / RESTORE ###

# backup:
# 	@mkdir -p $(BACKUP_DIR)
# 	docker exec $(DB_CONTAINER) pg_dump -U $$POSTGRES_USER $(DB) > $(BACKUP_DIR)/backup_$(DATE).dump
# 	@echo "✔ Backup created in $(BACKUP_DIR)"

restore:
# ifndef FILE
# 	$(error ❗ Укажи файл: make restore FILE=backups/xxx.dump)
# endif
# 	docker exec -i $(DB_CONTAINER) psql -U $$POSTGRES_USER postgres -c "DROP DATABASE IF EXISTS $(DB)"
# 	docker exec -i $(DB_CONTAINER) psql -U $$POSTGRES_USER postgres -c "CREATE DATABASE $(DB)"
# 	cat $(FILE) | docker exec -i $(DB_CONTAINER) psql -U $$POSTGRES_USER $(DB)
# 	@echo "✔ Database restored"
