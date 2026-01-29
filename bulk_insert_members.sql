-- ============================================================================
-- Script de Inserção em Lote de Membros
-- ============================================================================
-- Este script insere múltiplos membros no banco de dados de uma só vez
-- Certifique-se de ajustar os valores de acordo com os seus dados reais
-- ============================================================================

INSERT INTO
    cadmember_member (
        name,
        cpf,
        date_birth,
        city_birth,
        state_birth,
        date_baptism,
        address,
        cep,
        bairro,
        city,
        state,
        dizimista,
        telephone,
        created_at,
        updated_at
    )
VALUES
    -- Membro 1
    (
        'João Silva Santos',
        '12345678901',
        '1980-05-15',
        'São Paulo',
        'SP',
        '1995-08-20',
        'Rua das Flores, 123',
        '01310100',
        'Centro',
        'São Paulo',
        'SP',
        1,
        '11987654321',
        '2026-01-26 10:00:00',
        '2026-01-26 10:00:00'
    ),
    -- Membro 2
    (w
        'Maria Oliveira Costa',
        '98765432101',
        '1985-09-22',
        'Rio de Janeiro',
        'RJ',
        '2000-11-10',
        'Avenida Paulista, 500',
        '01310200',
        'Bela Vista',
        'São Paulo',
        'SP',
        1,
        '11988776655',
        '2026-01-26 10:01:00',
        '2026-01-26 10:01:00'
    ),
    -- Membro 3
    (
        'Carlos Mendes Ferreira',
        '55544433322',
        '1990-03-10',
        'Belo Horizonte',
        'MG',
        '2005-06-15',
        'Rua das Pedras, 789',
        '30130100',
        'Funcionários',
        'Belo Horizonte',
        'MG',
        0,
        '31987654321',
        '2026-01-26 10:02:00',
        '2026-01-26 10:02:00'
    ),
    -- Membro 4
    (
        'Ana Paula Rodrigues',
        '11122233344',
        '1988-07-08',
        'Salvador',
        'BA',
        '2003-09-20',
        'Avenida Costa, 456',
        '40140160',
        'Ondina',
        'Salvador',
        'BA',
        1,
        '71987654321',
        '2026-01-26 10:03:00',
        '2026-01-26 10:03:00'
    ),
    -- Membro 5
    (
        'Pedro Gonçalves Lima',
        '99988877766',
        '1975-12-03',
        'Brasília',
        'DF',
        '1992-01-25',
        'Quadra 506, Bloco A',
        '70340000',
        'Asa Norte',
        'Brasília',
        'DF',
        1,
        '61987654321',
        '2026-01-26 10:04:00',
        '2026-01-26 10:04:00'
    );

-- ============================================================================
-- Notas Importantes:
-- ============================================================================
-- 1. Certifique-se de que os CPFs são únicos (UNIQUE constraint)
-- 2. Os campos obrigatórios são: name, cpf, date_birth, date_baptism, address, cep
-- 3. Os campos opcionais podem ter NULL: city_birth, state_birth, bairro, city, state, telephone
-- 4. O campo dizimista é um booleano (0 = False, 1 = True)
-- 5. Os campos created_at e updated_at serão preenchidos automaticamente pelo Django se não especificados
-- 6. As datas devem estar no formato 'YYYY-MM-DD HH:MM:SS'
-- ============================================================================

-- ============================================================================
-- ALTERNATIVA COM DADOS INCOMPLETOS (para membros com dados parciais):
-- ============================================================================
/*
INSERT INTO cadmember_member (
name,
cpf,
date_birth,
date_baptism,
address,
cep,
dizimista,
created_at,
updated_at
) VALUES
(
'Membro Sem Dados Completos',
'44455566677',
'1992-04-14',
'2010-05-30',
'Rua Exemplo, 999',
'02310100',
0,
'2026-01-26 10:05:00',
'2026-01-26 10:05:00'
);
*/