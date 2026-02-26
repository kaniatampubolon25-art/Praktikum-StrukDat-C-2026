hanya_coding = ukm_coding - ukm_robotik
print("Hanya mendaftar coding :", hanya_coding)

seluruh_mahasiswa = ukm_coding | ukm_robotik
print("Seluruh mahasiwa uknik :", seluruh_mahasiswa)

andi_robotik = "Andi" in ukm_robotik
print("Apakah Andi anggota robotik?", andi_robotik)