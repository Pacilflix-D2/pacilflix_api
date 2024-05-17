-- Trigger biru
-- ISI DISINI
-- Trigger hijau
-- ISI DISINI
-- Trigger kuning
-- ISI DISINI
-- Trigger merah
CREATE
OR REPLACE FUNCTION buy_subscription () RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS((SELECT 1 FROM transaction t WHERE t.username = new.username AND t.end_date_time >= current_date)) THEN
        UPDATE transaction
        SET end_date_time = new.end_date_time,
            start_date_time = new.start_date_time,
            nama_paket = new.nama_paket,
            metode_pembayaran = new.metode_pembayaran,
            timestamp_pembayaran = new.timestamp_pembayaran
        WHERE username = new.username AND end_date_time = (SELECT MAX(end_date_time) FROM transaction WHERE username = new.username);
        RETURN NULL;
    ELSE
        RETURN NEW;
    END IF;
END
$$ LANGUAGE plpgsql
;

DROP TRIGGER IF EXISTS buy_subscription ON TRANSACTION
;

CREATE TRIGGER buy_subscription BEFORE INSERT ON TRANSACTION FOR EACH ROW
EXECUTE FUNCTION buy_subscription ()
;