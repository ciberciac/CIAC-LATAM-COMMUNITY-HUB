// Título:            Borrado de shadow copies con vssadmin
// ATT&CK:            T1490
// Dataset:           xdr_data
// Sigma equivalente: sigma/windows/proc_creation_win_vssadmin_borrado_shadow.yml
// Falsos positivos:  Software de copias de seguridad que gestiona instantáneas
// Estado:            experimental
// Autor / fecha:     CIAC LATAM Community / 2026-11-14
dataset = xdr_data
| filter event_type = ENUM.PROCESS and event_sub_type = ENUM.PROCESS_START
| filter lowercase(action_process_image_name) = "vssadmin.exe"
| filter lowercase(action_process_image_command_line) contains "delete"
    and lowercase(action_process_image_command_line) contains "shadows"
| fields _time, agent_hostname, actor_effective_username,
         action_process_image_command_line, actor_process_image_name
