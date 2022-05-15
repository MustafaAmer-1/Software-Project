

from flask import (
    Blueprint, render_template, 
)

from app.services.ticket_service import sum_tickets_by_month


statistics_manage = Blueprint('statistics_manage', __name__)

@statistics_manage.route('/statistics')
def statistics():

    revenue_per_month = [0 for _ in range(12)]


    for month, summation in sum_tickets_by_month():
        revenue_per_month[month - 1] = summation

    # print(revenue_per_month)
    return render_template('statistics.html', revenue=revenue_per_month)
