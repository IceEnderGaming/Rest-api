
from data import db_session
from data.jobs import Jobs
from flask import Blueprint, jsonify, make_response


blueprint = Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_news(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    if not jobs or job_id > len(jobs) - 1:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs':
                jobs[job_id].to_dict(only=('user_id', 'activity', 'team_leader', 'work_size', 'collaborators', 'is_finished'))
        }
    )
