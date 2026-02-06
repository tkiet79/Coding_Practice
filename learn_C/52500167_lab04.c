#include <stdio.h>
#define MAX 10

void sapXepGiamDan(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                // Hoán vị (Swap)
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int xoaTrung(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                for (int k = j; k < n - 1; k++) {
                    arr[k] = arr[k + 1];
                }
                n--; 
                j--; 
            }
        }
    }
    return n;
}

void nhanMaTran(int A[MAX][MAX], int B[MAX][MAX], int C[MAX][MAX], int rA, int cA, int cB) {
    for (int i = 0; i < rA; i++) {
        for (int j = 0; j < cB; j++) {
            C[i][j] = 0;
            for (int k = 0; k < cA; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void chuyenVi(int A[MAX][MAX], int T[MAX][MAX], int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            T[j][i] = A[i][j];
        }
    }
}

int dinhThuc2x2(int m[MAX][MAX]) {
    return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0]);
}

int main() {
    int n, rA, cA, rB, cB;
    int mang[MAX];
    int A[MAX][MAX], B[MAX][MAX], KQ[MAX][MAX];

    printf("--- CHUONG TRINH QUAN LY MANG VA MA TRAN ---\n");

    // --- NHẬP VÀ XỬ LÝ MẢNG ---
    printf("\n[1] Nhap so phan tu cua mang (toi da %d): ", MAX);
    scanf("%d", &n);
    if (n > MAX || n <= 0) {
        printf(" Nhap sai so luong roi!\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        printf("Nhap mang[%d]: ", i);
        scanf("%d", &mang[i]);
    }

    sapXepGiamDan(mang, n);
    n = xoaTrung(mang, n);

    printf("=> Mang sau khi sap xep va xoa trung: ");
    for (int i = 0; i < n; i++) printf("%d ", mang[i]);

    // --- NHẬP VÀ XỬ LÝ MA TRẬN ---
    printf("\n\n[2] Nhap kich thuoc ma tran A (hang cot): ");
    scanf("%d %d", &rA, &cA);
    
    printf("Nhap cac phan tu ma tran A:\n");
    for (int i = 0; i < rA; i++) {
        for (int j = 0; j < cA; j++) {
            printf("A[%d][%d]: ", i, j);
            scanf("%d", &A[i][j]);
        }
    }

    // Tinh dinh thuc neu la 2x2
    if (rA == 2 && cA == 2) {
        printf("=> Dinh thuc ma tran A (2x2): %d\n", dinhThuc2x2(A));
    }

    // Chuyen vi ma tran A
    int T[MAX][MAX];
    chuyenVi(A, T, rA, cA);
    printf("=> Ma tran chuyen vi cua A:\n");
    for (int i = 0; i < cA; i++) {
        for (int j = 0; j < rA; j++) printf("%d ", T[i][j]);
        printf("\n");
    }

    // Nhan ma tran (Neu thoa man dieu kien)
    printf("\n[3] Nhap kich thuoc ma tran B (hang cot): ");
    scanf("%d %d", &rB, &cB);

    if (cA != rB) {
        printf("Loi: So cot cua A phai bang so hang cua B de nhan ma tran!\n");
    } else {
        printf("Nhap cac phan tu ma tran B:\n");
        for (int i = 0; i < rB; i++) {
            for (int j = 0; j < cB; j++) {
                printf("B[%d][%d]: ", i, j);
                scanf("%d", &B[i][j]);
            }
        }

        nhanMaTran(A, B, KQ, rA, cA, cB);
        printf("=> Ket qua A * B:\n");
        for (int i = 0; i < rA; i++) {
            for (int j = 0; j < cB; j++) printf("%d ", KQ[i][j]);
            printf("\n");
        }
    }

    return 0;
}