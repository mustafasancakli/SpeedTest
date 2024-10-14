import streamlit as st
import speedtest

st.title("İnternet Hız Testi")

st_test = speedtest.Speedtest()

if st.button("Hız testini hemen başlat."):
    st.write("Bekle! Hızını ölçüyorum.")

    # Sunucu seçmek için
    st_test.get_servers()
    best_server = st_test.get_best_server()
    st.write(f"Seçilen sunucu: {best_server['host']} ({best_server['country']})")

    # Download hızı
    download_speed = st_test.download() / 1000000  # Mbps'e çevrildi
    st.write(f"İndirme hızı: {download_speed:.2f} Mbps")

    # Upload hızı
    upload_speed = st_test.upload() / 1000000  # Mbps'e çevrildi
    st.write(f"Yükleme hızı: {upload_speed:.2f} Mbps")

    # Ping
    ping = st_test.results.ping
    st.write(f"Ping: {ping:.2f} ms")
