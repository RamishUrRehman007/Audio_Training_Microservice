BEGIN;

DO
$do$
DECLARE
    current_migration_number integer := 3;
BEGIN
    IF NOT EXISTS (SELECT migration_number FROM migrations WHERE migration_number = current_migration_number) THEN
        CREATE EXTENSION IF NOT EXISTS citext;
        CREATE TABLE model_predictions(
            id SERIAL PRIMARY KEY,
            audio_file_id INT NOT NULL REFERENCES audio_files(id),
            confidence_utterance CITEXT,
            confidence_time INT,
            confidence_value FLOAT,
            created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
            deleted_at TIMESTAMPTZ
        );

        INSERT INTO migrations(migration_number) VALUES (current_migration_number);
    ELSE
        RAISE NOTICE 'Already ran migration %.', current_migration_number;
    END IF;
END
$do$;

COMMIT;
