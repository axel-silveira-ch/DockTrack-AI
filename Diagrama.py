from graphviz import Digraph

dot = Digraph(comment='DocTrackAI Diagram', format='png')

# Configuración global
dot.attr(rankdir='LR')  # Direccionamiento horizontal
dot.attr('node', shape='plaintext')

# Pacientes
dot.node('Pacientes', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Pacientes</B></TD></TR>
<TR><TD>ID_Paciente: int</TD></TR>
<TR><TD>Nombre: varchar</TD></TR>
<TR><TD>Fecha_Nacimiento: date</TD></TR>
<TR><TD>Teléfono: varchar</TD></TR>
<TR><TD>Dirección: varchar</TD></TR>
</TABLE>>''')

# Médicos
dot.node('Medicos', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Médicos</B></TD></TR>
<TR><TD>ID_Medico: int</TD></TR>
<TR><TD>Nombre: varchar</TD></TR>
<TR><TD>Especialidad: varchar</TD></TR>
<TR><TD>Teléfono: varchar</TD></TR>
<TR><TD>Email: varchar</TD></TR>
</TABLE>>''')

# Citas
dot.node('Citas', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Citas</B></TD></TR>
<TR><TD>ID_Cita: int</TD></TR>
<TR><TD>ID_Paciente: int</TD></TR>
<TR><TD>Fecha: date</TD></TR>
<TR><TD>Motivo: varchar</TD></TR>
<TR><TD>Estado: varchar</TD></TR>
</TABLE>>''')

# Expedientes
dot.node('Expedientes', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Expedientes</B></TD></TR>
<TR><TD>ID_Expediente: int</TD></TR>
<TR><TD>ID_Paciente: int</TD></TR>
<TR><TD>Historial: text</TD></TR>
<TR><TD>Última_Actualización: timestamp</TD></TR>
</TABLE>>''')

# Diagnósticos
dot.node('Diagnosticos', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Diagnósticos</B></TD></TR>
<TR><TD>ID_Diagnostico: int</TD></TR>
<TR><TD>ID_Cita: int</TD></TR>
<TR><TD>Detalle: text</TD></TR>
<TR><TD>Fecha: date</TD></TR>
</TABLE>>''')

# Horarios
dot.node('Horarios', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Horarios</B></TD></TR>
<TR><TD>ID_Horario: int</TD></TR>
<TR><TD>ID_Medico: int</TD></TR>
<TR><TD>Día: varchar</TD></TR>
<TR><TD>Hora_Inicio: time</TD></TR>
<TR><TD>Hora_Fin: time</TD></TR>
</TABLE>>''')

# Administración
dot.node('Administracion', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Administración</B></TD></TR>
<TR><TD>ID_Usuario: int</TD></TR>
<TR><TD>Nombre: varchar</TD></TR>
<TR><TD>Rol: varchar</TD></TR>
<TR><TD>Contraseña: varchar</TD></TR>
</TABLE>>''')

# Facturas
dot.node('Facturas', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Facturas</B></TD></TR>
<TR><TD>ID_Factura: int</TD></TR>
<TR><TD>ID_Cita: int</TD></TR>
<TR><TD>Monto: float</TD></TR>
<TR><TD>Fecha_Emisión: date</TD></TR>
</TABLE>>''')

# Alertas
dot.node('Alertas', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Alertas</B></TD></TR>
<TR><TD>ID_Alerta: int</TD></TR>
<TR><TD>Mensaje: text</TD></TR>
<TR><TD>Enviado: boolean</TD></TR>
</TABLE>>''')

# Reportes
dot.node('Reportes', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="1"><B>Reportes</B></TD></TR>
<TR><TD>ID_Reporte: int</TD></TR>
<TR><TD>Contenido: text</TD></TR>
<TR><TD>Fecha: date</TD></TR>
</TABLE>>''')

# Relaciones entre nodos
dot.edge('Pacientes', 'Citas', label='programa')
dot.edge('Citas', 'Expedientes', label='actualiza')
dot.edge('Citas', 'Diagnosticos', label='actualiza')
dot.edge('Diagnosticos', 'Expedientes', label='actualiza')
dot.edge('Medicos', 'Citas', label='atiende')
dot.edge('Medicos', 'Horarios', label='autoriza')
dot.edge('Administracion', 'Facturas', label='genera')
dot.edge('Administracion', 'Reportes', label='informa a')
dot.edge('Reportes', 'Alertas', label='resumen de')
dot.edge('Facturas', 'Citas', label='corresponde a')

# Renderizar y guardar
dot.render('DocTrackAI_Updated_Diagram', view=True)
