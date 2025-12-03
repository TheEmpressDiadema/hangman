class StageGraphics:

    stages = [
        '''
                 |
                 |
                 |
                 |
                 /\\
        ''',
        '''
         --------|
                 |
                 |
                 |
                 /\\
        ''',
        '''
         --------|
         |       |
                 |
                 |
                 /\\
        ''',
        '''
         --------|
         |       |
         O       |
                 |
                 /\\
        ''',
        '''
         --------|
         |       |
         O       |
        /|\\     |
                /\\
        ''',
        '''
         --------|
         |       |
         O       |
        /|\\     |
         /\\       /\\
        '''
    ]

    @classmethod
    def get_stage(cls, mistake_index: int) -> str:
        return cls.stages[mistake_index]