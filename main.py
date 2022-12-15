class CpfValidator:
    def __init__(self, cpf: str) -> None:
        self.cpf = cpf
        self.verified_cpf = self.validate()
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        cpf = ''.join(list(map(lambda i: i if i.isnumeric() else '', cpf)))
        self._cpf = cpf
    
    def calculate_first_digit(self) -> str:
        """Calcula o primeiro digito do cpf

        Returns:
            str: reultado do calculo do primeiro digito.
        """
        result, m = 0, 10
        for c in self.cpf[:-2]:
            calc = int(c) * m
            result += calc
            m -= 1

        final_result = str(11 - result % 11)
        return final_result if int(final_result) <= 9 else '0'


    def calculate_second_digit(self) -> str:
        """Calcula o segundo digito do cpf

        Returns:
            str: resultado do calculo do segundo digito.
        """
        m, ac = 11, 0
        for i in self.cpf[:-2] + self.calculate_first_digit():
            calc = int(i) * m
            ac += calc
            m -= 1

        final_result = str(11 - ac % 11)
        return final_result if int(final_result) <= 9 else '0'

    def validate(self) -> str:
        """Faz verificação de comprimento e sequencia, execulta os calculos do
        primeiro e segundo digito, e forma o cpf para validação.

        Returns:
            str: cpf com calculo do primeiro e segundo digito para validar
        """
        if self.is_sequence() or not self.has_valid_length():
            return False
        base = self.cpf[:-2]
        first_digit = self.calculate_first_digit()
        second_digit = self.calculate_second_digit()
        cpf_to_validation = base + first_digit + second_digit
        return cpf_to_validation

    def is_valid(self) -> bool:
        """verifica se o cpf enviado é valido

        Returns:
            bool: True se o cpf é valido ou False se não é valido.
        """
        return True if self.cpf == self.verified_cpf else False
    
    def is_sequence(self) -> bool:
        """Verifica se o cpf enviado é uma sequencia Ex; 000.000.000-00

        Returns:
            bool: True se for uma sequencia de digitos, False se não for
        """
        verify = self.cpf[0] * 11
        return True if verify == self.cpf else False
    
    def has_valid_length(self) -> bool:
        """Verifica se o comprimento do cpf enviado é valido.

        Returns:
            bool: True se o comprimento for valido ou False se não é valido.
        """
        return True if len(self.cpf) == 11 else False


if __name__ == '__main__':
    cpf_base = input('CPF: ')
    cpf_validation = CpfValidator(cpf_base)
    result = 'valid' if cpf_validation.is_valid() else 'invalid'
    print(f'the sent cpf is {result}')
