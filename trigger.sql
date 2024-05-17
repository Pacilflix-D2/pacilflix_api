-- Trigger biru
-- ISI DISINI
CREATE
OR REPLACE FUNCTION check_username_exists () RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM PENGGUNA WHERE username = NEW.username) THEN
        RAISE EXCEPTION 'Error: Username already exists';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql
;

CREATE TRIGGER before_insert_pengguna BEFORE INSERT ON PENGGUNA FOR EACH ROW
EXECUTE FUNCTION check_username_exists ()
;

-- Trigger hijau
CREATE
OR REPLACE FUNCTION check_if_user_already_sent_review () RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM ULASAN WHERE id_tayangan = NEW.id_tayangan AND username = NEW.username) THEN
        RETURN NEW;
    ELSE
        RAISE EXCEPTION 'Gagal membuat ulasan. Anda sudah menulis ulasan di tayangan ini.';
    END IF;
END;
$$ LANGUAGE plpgsql
;

CREATE TRIGGER check_if_user_already_sent_review_trigger BEFORE INSERT ON ULASAN FOR EACH ROW
EXECUTE FUNCTION check_if_user_already_sent_review ()
;

-- Trigger kuning
CREATE
OR REPLACE FUNCTION validate_delete_downloaded_shows () RETURNS TRIGGER AS $$
BEGIN
    IF OLD.timestamp BETWEEN (CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Jakarta') - INTERVAL '24 hours' AND
                               (CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Jakarta') THEN
        RAISE EXCEPTION 'Tayangan yang baru diunduh kurang dari 1 hari tidak dapat dihapus';
    ELSE
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql
;

CREATE TRIGGER verify_delete_downloaded_shows BEFORE DELETE ON TAYANGAN_TERUNDUH FOR EACH ROW
EXECUTE FUNCTION validate_delete_downloaded_shows ()
;

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