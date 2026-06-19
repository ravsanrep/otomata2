# Pushdown Automata (PDA) Simulator

## Anggota Kelompok

| No | Nama | NRP |
|----|------|-----|
| 1 | Muhammad Sayyidil Anam | 5025241267 |
| 2 | Abdurrahman Arrafi | 5025241241 |
| 3 | Antonius Andy Martono | 5025241191 |

## Deskripsi Program

Program ini merupakan simulasi **Pushdown Automata (PDA)** yang dibuat menggunakan Python dan library Tkinter. PDA yang diimplementasikan digunakan untuk mengenali bahasa:

**L = { aⁿbⁿ | n ≥ 1 }**

Artinya jumlah simbol `a` harus sama dengan jumlah simbol `b`, dengan seluruh `a` muncul terlebih dahulu sebelum `b`.

Contoh string yang diterima:

* `ab`
* `aabb`
* `aaabbb`

Contoh string yang ditolak:

* `aab`
* `abb`
* `ba`
* `abab`

---

## Fitur Program

* Input string secara langsung melalui GUI.
* Simulasi operasi **Push** dan **Pop** pada stack.
* Menampilkan isi stack selama proses berjalan.
* Menampilkan riwayat proses pembacaan simbol.
* Menampilkan hasil akhir berupa **ACCEPTED** atau **REJECTED**.
* Tombol reset untuk mengembalikan tampilan ke kondisi awal.

---


### Jalankan program

```bash
python pda.py
```


## Cara Penggunaan

1. Masukkan string pada kolom **Input String**.
2. Klik tombol **Process**.
3. Program akan memproses string sesuai aturan PDA.
4. Hasil proses akan ditampilkan pada bagian:

   * Process History
   * Stack
   * Status ACCEPTED atau REJECTED
5. Klik **Reset** untuk mengosongkan input dan hasil sebelumnya.

---

## Konsep PDA yang Digunakan

Program menggunakan dua state:

* **q0** → membaca simbol `a` dan melakukan **PUSH** ke stack.
* **q1** → membaca simbol `b` dan melakukan **POP** dari stack.

Aturan utama:

* Setiap simbol `a` menambahkan satu simbol `A` ke stack.
* Setiap simbol `b` menghapus satu simbol `A` dari stack.
* String diterima jika:

  * Seluruh input habis dibaca.
  * State akhir berada di `q1`.
  * Stack kosong.

---

## Contoh Pengujian

| Input  | Hasil    |
| ------ | -------- |
| ab     | ACCEPTED |
| aabb   | ACCEPTED |
| aaabbb | ACCEPTED |
| aab    | REJECTED |
| abb    | REJECTED |
| ba     | REJECTED |
| abab   | REJECTED |

---

## Teknologi yang Digunakan

* Python 3
* Tkinter (GUI)

---

## Kesimpulan

Program berhasil mensimulasikan Pushdown Automata untuk bahasa **L = { aⁿbⁿ | n ≥ 1 }** dengan memanfaatkan stack sebagai media penyimpanan simbol sementara. Program dapat menentukan apakah suatu string diterima atau ditolak sesuai aturan bahasa yang telah ditentukan.
