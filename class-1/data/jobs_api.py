
from data import db_session
from data.jobs import Jobs
from flask import Blueprint, jsonify


blueprint = Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('user_id', 'activity', 'team_leader', 'work_size', 'collaborators', 'is_finished'))
                 for item in jobs]
        }
    )
