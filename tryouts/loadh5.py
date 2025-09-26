import h5py
with h5py.File('data-project-1-classification-2025-2-b/train.h5', 'r') as f:
    print(list(f.keys()))  # Verifica los nombres de los datasets


# import h5py
# with h5py.File('data-project-1-classification-2025-2-b/train.h5', 'r') as f:
#     data = f['data'][:]  # Series de tiempo (ej: forma [n_muestras, 64_electrodos, 256_puntos_tiempo])
#     labels = f['label'][:]  # Etiquetas (0: control, 1: alcohólico)