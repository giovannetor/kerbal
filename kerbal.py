import krpc
conn = krpc.connect(name = "Test")
vessel = conn.space_center.active_vessel
