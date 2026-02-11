tim_frontend = {"HTML", "CSS", "JavaScript", "Reatct"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

irisan= tim_frontend.intersection(tim_backend)
print(irisan)

backend_only = tim_backend.difference(tim_frontend)
print(backend_only)

gabungan = tim_frontend | tim_backend
print(gabungan)