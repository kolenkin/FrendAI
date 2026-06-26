from pathlib import Path

# ==========================
# Настройки
# ==========================

BACKUP = Path(r"D:\FrendAi\BackUP\backup16.bin")
OUTDIR = Path(r"D:\FrendAi\Extracted")

PARTITIONS = [
    ("nvs.bin",    0x9000,   0x4000),
    ("otadata.bin",0xD000,   0x2000),
    ("phy_init.bin",0xF000,  0x1000),
    ("model.bin",  0x10000,  0xF0000),
    ("ota0.bin",   0x100000, 0x600000),
    ("ota1.bin",   0x700000, 0x600000),
]

# ==========================

OUTDIR.mkdir(exist_ok=True)

size = BACKUP.stat().st_size

print("=" * 60)
print("ESP32 Flash Extractor")
print("=" * 60)
print(f"Backup : {BACKUP}")
print(f"Size   : {size:,} bytes")
print()

with BACKUP.open("rb") as f:

    for name, offset, length in PARTITIONS:

        print(f"[+] {name}")

        f.seek(offset)

        data = f.read(length)

        outfile = OUTDIR / name

        outfile.write_bytes(data)

        print(f"    Offset : 0x{offset:08X}")
        print(f"    Size   : {length:,} bytes")
        print(f"    Saved  : {outfile}")
        print()

print("=" * 60)
print("Done.")
print("=" * 60)