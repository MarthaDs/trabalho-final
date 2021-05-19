import random
from django import template

register = template.Library()

@register.simple_tag
def random_job(race):
    job_for_white = ('Engenheira', 'Médica','Advogada', 'Hedeira')
    job_for_black = ('Doméstica', 'Atendente de Telemarketing', 'Agente de Limpeza/Segurança',
        'Desempregada')
    
    if race == 'white':
        return random.choice(job_for_white)
    return random.choice(job_for_black)