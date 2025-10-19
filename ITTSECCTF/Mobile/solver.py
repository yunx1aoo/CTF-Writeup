 private void tampilkanLaporan() {
        DefaultTableModel model = (DefaultTableModel) tbl_laporan.getModel();
        model.setRowCount(0);
        
        for(int i = 0; i < transaksi.listPelanggan.size(); i++) {
            model.addRow(new Object[] {
            transaksi.listPelanggan.get(i),
            transaksi.listLayanan.get(i),
            transaksi.listJumlah.get(i),
            transaksi.listTotal.get(i),
            transaksi.listStatus.get(i)
            });
        }
    }
    
    private void ringkasan() {
        int total_transaksi = transaksi.listPelanggan.size();
        int total_pendapatan = 0;
        for (int i = 0; i < transaksi.listTotal.size(); i++) {
            total_pendapatan += transaksi.listTotal.get(i);
        }
        
        int selesai = 0;
        int proses = 0;
        int menunggu = 0;
        
        for(int i = 0; i < transaksi.listStatus.size(); i++) {
            String status = transaksi.listStatus.get(i);
            
            if(status.equalsIgnoreCase("selesai")) {
                selesai++;
            } else if(status.equalsIgnoreCase("Di proses")) {
                proses++;
            } else if(status.equalsIgnoreCase("Menunggu")) {
                menunggu++;
            }
        }
        j_total_transaksi.setText("Total Transaksi: " + total_transaksi + " Transaksi");
        pendapatan_l.setText("Total Pendapatan: " + total_pendapatan + " Pendapatan");
        selesai_l.setText("Total Selesai: " + selesai + " Transaksi");
        selesai_l.setText("Total Diproses: " + proses + " Transaksi");
        selesai_l.setText("Total Menunggu: " + menunggu + " Transaksi");
    }

 public static ArrayList<String> listLayanan = new ArrayList<>();
    public static ArrayList<Integer> listHarga = new ArrayList<>();
    int selectedIndex = -1;

  private void tampilkanData(){
        DefaultTableModel model = (DefaultTableModel) tbl_layanan.getModel();
        model.setRowCount(0);
        
        for(int i = 0; i < listLayanan.size(); i++) {
            model.addRow(new Object[]{
                listLayanan.get(i),
                listHarga.get(i)
            });
        }
    }
    
    
    private void clearForm(){
        txt_layanan.setText("");
        txt_harga.setText("");
        selectedIndex = -1;
        tbl_layanan.clearSelection();
    }
    
    private void simpanData(){
        String layanan = txt_layanan.getText();
        String hargastr = txt_harga.getText();
        
        if (layanan.isEmpty() || hargastr.isEmpty()){
            JOptionPane.showMessageDialog(this, "Terdapat data yang kosong! Harap isi semua data!");
            return;
        }
        
        int harga;
        
        try{
            harga = Integer.parseInt(hargastr);
            
            if(harga <= 0) {
                JOptionPane.showMessageDialog(this, "harap masukkan harga lebih dari 0");
                return;
            }
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "harap masukkan angka yang valid!");
            return;
        }
        
        if(selectedIndex >= 0 ){
            for(int i = 0; i < listLayanan.size(); i++){
                if(i != selectedIndex && listLayanan.get(i).equalsIgnoreCase(layanan)){
                    JOptionPane.showMessageDialog(this, "layanan sudah terdaftar");
                    return;
                }
            }
            listLayanan.set(selectedIndex, layanan);
            listHarga.set(selectedIndex, harga);
        } else {
            for(int i = 0; i < listLayanan.size(); i++) {
                if (listLayanan.get(i).equalsIgnoreCase(layanan)) {
                    JOptionPane.showMessageDialog(this, "layanan sudah terdaftar");
                    return;
                }
            }
            listLayanan.add(layanan);
            listHarga.add(harga);
            JOptionPane.showMessageDialog(this, "data berhasil di tambahkan");
        }
        tampilkanData();
        clearForm();
    }

    private void clickedTable() {  
     selectedIndex = tbl_layanan.getSelectedRow();
     if (selectedIndex >= 0) {
         txt_layanan.setText(listLayanan.get(selectedIndex));
         txt_harga.setText(String.valueOf(listHarga.get(selectedIndex)));
     }
    }
    
    private void hapusData(){
        if (selectedIndex <= 0 ) {
            JOptionPane.showMessageDialog(this, "harap pilih data yang ingin di hapus");
            return;
        }
        
        int confirm = JOptionPane.showConfirmDialog(this,
                "apakah anda yakin ingin menghapus data ini?",
                "konfirmasi hapus",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.WARNING_MESSAGE);
        
        if (confirm == JOptionPane.YES_OPTION) {
            listLayanan.remove(selectedIndex);
            listHarga.remove(selectedIndex);
        }
        tampilkanData();
        clearForm();
        JOptionPane.showMessageDialog(this, "data berhasill di hapus!");
    }
 private void clickedTable() {
        selectedIndex = tbl_transaksi.getSelectedRow();
        
        if (selectedIndex >= 0) {
            combo_status.setSelectedItem(tbl_transaksi.getValueAt(selectedIndex, 4).toString());
        }
    }

    private void loadpelanggan() {
        combo_pelanggan.removeAllItems();
        combo_pelanggan.addItem("--pilih pelanggan--");
        for (int i = 0; i < pelanggan.listNama.size(); i++) {
            String item = pelanggan.listNama.get(i) + "-" + pelanggan.listPlat.get(i);
            combo_pelanggan.addItem(item);
        }
    }

    private void tampilkanDataPelanggan() {
        DefaultTableModel model = (DefaultTableModel) tbl_pelanggan.getModel();
        model.setRowCount(0);

        for (int i = 0; i < pelanggan.listNama.size(); i++) {
            model.addRow(new Object[]{
                pelanggan.listNama.get(i),
                pelanggan.listTelp.get(i),
                pelanggan.listAlamat.get(i),
                pelanggan.listJenis.get(i),
                pelanggan.listPlat.get(i),});
        }
    }

    private void loadlayanan() {
        combo_layanan.removeAllItems();
        combo_layanan.addItem("--Pilih Layanan--");

        for (int i = 0; i < layanan.listLayanan.size(); i++) {
            String item = layanan.listLayanan.get(i) + "-" + layanan.listHarga.get(i);
            combo_layanan.addItem(item);
        }
    }

    private void tampilkanLayanan() {
        DefaultTableModel model = (DefaultTableModel) tbl_layanan.getModel();
        model.setRowCount(0);

        for (int i = 0; i < layanan.listLayanan.size(); i++) {
            model.addRow(new Object[]{
                layanan.listLayanan.get(i),
                layanan.listHarga.get(i)
            });
        }

    }
    
    private void clearFrom() {
        combo_pelanggan.setSelectedIndex(0);
        combo_layanan.setSelectedIndex(0);
        combo_status.setSelectedIndex(0);
        txt_jumlah.setText("");
        txt_total.setText("");
    }
    
    private void status() {
        combo_status.removeAllItems();
        combo_status.addItem("--Pilih Status--");
        combo_status.addItem("Di proses");
        combo_status.addItem("Menunggu");
        combo_status.addItem("selesai");
    }
    
    private void tampilkanTransaksi(){
        DefaultTableModel model = (DefaultTableModel) tbl_transaksi.getModel();
        model.setRowCount(0);
        
        for (int i = 0; i < listPelanggan.size(); i++) {
           model.addRow(new Object[]{
           listPelanggan.get(i),
           listLayanan.get(i),
           listJumlah.get(i),
           listTotal.get(i),
           listStatus.get(i)
           });
        }
    }

    private void hitungTotal() {
        if (combo_pelanggan.getSelectedIndex() == 0) {
            JOptionPane.showMessageDialog(this, "harap pilih pelanggan", "peringatan", JOptionPane.WARNING_MESSAGE);
            return;
        }

        if (combo_layanan.getSelectedIndex() == 0) {
            JOptionPane.showMessageDialog(this, "harap pilih layanan", "peringatan", JOptionPane.WARNING_MESSAGE);
            return;
        }

        if (txt_jumlah.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "harap masukkan jumlah", "peringatan", JOptionPane.WARNING_MESSAGE);
            return;
        }

        int jumlah = Integer.parseInt(txt_jumlah.getText());

        if (jumlah <= 0) {
            JOptionPane.showMessageDialog(this, "jumlah harus lebih dari 0");
        }
        
        int idxlayanan = combo_layanan.getSelectedIndex() - 1;
        
        int harga = layanan.listHarga.get(idxlayanan);
        
        int total = harga * jumlah;
        
        txt_total.setText(String.valueOf(total));

    }
    
    private void simpanTransaksi() {
        String dataPelanggan = combo_pelanggan.getSelectedItem().toString();
        String[] splitPelanggan = dataPelanggan.split("-");
        String namaPelanggan = splitPelanggan[0].trim();
        
        String dataLayanan = combo_layanan.getSelectedItem().toString();
        String[] splitLayanan = dataLayanan.split("-");
        String namaLayanan = splitLayanan[0].trim();
        
        int jumlah = Integer.parseInt(txt_jumlah.getText());
        int total = Integer.parseInt(txt_total.getText());
        
        String status = combo_status.getSelectedItem().toString();
        
        listPelanggan.add(namaPelanggan);
        listLayanan.add(namaLayanan);
        listJumlah.add(jumlah);
        listTotal.add(total);
        listStatus.add(status);
        
        clearFrom();
        tampilkanTransaksi();
    }
