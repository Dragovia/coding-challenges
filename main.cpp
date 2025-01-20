
#include <immintrin.h>
#include <iostream>
#include <vector>
#include <iomanip>

class AVX512Multiplier {
public:
    // Constructor
    AVX512Multiplier() {}

    // Function to perform SIMD multiplication
    std::vector<__int128> simdMultiply(const std::vector<uint64_t>& a, const std::vector<uint64_t>& b) {
        if (a.size() != 4 || b.size() != 4) {
            throw std::invalid_argument("Input vectors must have exactly 4 elements.");
        }

        // Load 64-bit integers into 512-bit registers
        __m512i va = _mm512_set_epi64(a[3], a[2], a[1], a[0], 0, 0, 0, 0);
        __m512i vb = _mm512_set_epi64(b[3], b[2], b[1], b[0], 0, 0, 0, 0);

        // Perform 64-bit multiplication on the lower parts
        __m512i low_result = _mm512_mul_epu32(va, vb);  // Multiply even-indexed elements of the vectors

        // Perform 64-bit multiplication on the higher parts
        __m512i high_result = _mm512_mul_epu32(_mm512_srli_epi64(va, 32), _mm512_srli_epi64(vb, 32));  // Multiply odd-indexed elements

        // Store the results back into a vector
        std::vector<__int128> result(4);

        // Extract results from the SIMD registers
        result[0] = (static_cast<__int128>(_mm512_extract_epi64(low_result, 0)) << 64) | _mm512_extract_epi64(low_result, 1);
        result[1] = (static_cast<__int128>(_mm512_extract_epi64(low_result, 2)) << 64) | _mm512_extract_epi64(low_result, 3);
        result[2] = (static_cast<__int128>(_mm512_extract_epi64(low_result, 4)) << 64) | _mm512_extract_epi64(low_result, 5);
        result[3] = (static_cast<__int128>(_mm512_extract_epi64(low_result, 6)) << 64) | _mm512_extract_epi64(low_result, 7);

        return result;
    }
};

int main() {
    // Test vectors
    std::vector<uint64_t> a = { 0x123456789ABCDEF0, 0xFEDCBA9876543210, 0x1111111111111111, 0x2222222222222222 };
    std::vector<uint64_t> b = { 0x0000000000000001, 0x0000000000000002, 0x0000000000000003, 0x0000000000000004 };

    // Expected results
    std::vector<__int128> expected_results = {
        0x123456789ABCDEF0,
        0x1FDB97530ECA86420,
        0x3333333333333333,
        0x8888888888888888
    };

    // Create the AVX-512 multiplier
    AVX512Multiplier multiplier;

    // Perform SIMD multiplication
    std::vector<__int128> results = multiplier.simdMultiply(a, b);

    // Print intermediate and final results
    bool pass = true;
    for (size_t i = 0; i < results.size(); i++) {
        std::cout << "Result " << i + 1 << ": 0x" << std::hex << results[i] << std::endl;
        if (results[i] != expected_results[i]) {
            pass = false;
        }
    }

    if (pass) {
        std::cout << "Test passed!" << std::endl;
    } else {
        std::cout << "Test failed!" << std::endl;
    }

    return 0;
}
