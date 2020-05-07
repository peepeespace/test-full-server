CREATE TRIGGER controlstate_changed
AFTER INSERT OR UPDATE
ON data_controlstate
FOR EACH ROW
EXECUTE PROCEDURE notify_controlstate_changes()