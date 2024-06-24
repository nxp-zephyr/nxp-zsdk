/**
 *  Copyright 2023-2024 NXP
 *
 *  SPDX-License-Identifier: Apache-2.0
 *
 */


#define MBEDTLS_PSA_CRYPTO_DRIVERS
#define PSA_CRYPTO_DRIVER_ELS_PKC

/* Entropy related configs */
#define MBEDTLS_ENTROPY_HARDWARE_ALT
#undef MBEDTLS_NO_DEFAULT_ENTROPY_SOURCES
