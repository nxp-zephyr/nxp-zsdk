[Index page](../getting-started-iw610-imxrt1060.md)\|[Build and flash examples](../topics/build_and_flash_examples.md)

# Build and flash in Ubuntu
## Wi-Fi shell example

This section shows how to compile the Wi-Fi shell example.

Step 1 - Build the application.

```
west build -b mimxrt1060_evk@C samples/net/wifi/shell -d iw610_wifi -p=always -DEXTRA_CONF_FILE="nxp/overlay_iw610.conf nxp/overlay_hostap_hosted_mcu.conf" --shield nxp_m2_2ll_wifi_bt

west build -b mimxrt1060_evk@C samples/net/wifi/shell -d wifi_shell

```

Step 2 - Flash the application.

```
export PATH=$PATH:/usr/local/LinkServer_24.12.21 #Change the Linkserver path
west flash --runner linkserver -d iw610_wifi
```

**Note:** To run the Wi-Fi shell application, refer to [Wi-Fi shell example](run_wi-fi_shell_example.md).

## Bluetooth shell example

This section shows how to compile the Bluetooth shell example.

Step 1 - Build the application.

```
cd ~/zephyrproject/zephyr
west build -p always -b mimxrt1060_evk@C --shield nxp_m2_2ll_wifi_bt ./tests/bluetooth/shell/ -d iw610_bt_shell
```

Step 2 - Flash the application.

```
export PATH=$PATH:/usr/local/LinkServer_24.12.21 //Change the Linkserver path
west flash --runner linkserver -d iw610_bt_shell
```

**Note:** To run the Bluetooth shell application, refer to [Bluetooth shell example](run_bluetooth_shell_example.md).

## Coexistence shell example

This section shows how to compile the Coexistence shell example.

Step 1 - Build the application.

```
cd ~/zephyrproject
west build -p always -b mimxrt1060_evk@C --shield nxp_m2_2ll_wifi_bt samples/wireless/coex/shell -d
coex_wifi_shell -DEXTRA_CONF_FILE="overlay-wifi-nxp-iw610.conf overlay-wifi-nxp-hostap-hosted-mcu.conf"
```

Step 2 - Flash the application.

```
export PATH=$PATH:/usr/local/LinkServer_24.12.21 # Change the Linkserver path
west flash --runner linkserver -d coex_wifi_shell
```

**Note:** To run the Coexistence shell application, refer to [Coexistence shell example](run_coexistence_shell_example.md).


**Parent topic:** [Build and flash examples](../topics/build_and_flash_examples.md)

