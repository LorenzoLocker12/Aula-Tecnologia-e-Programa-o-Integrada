from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
db = SQLAlchemy(app)

class Enquete(db.Model):
    enq_id = db.Column(db.Integer, primary_key=True)
    enq_title = db.Column(db.String(255), nullable=False)
    enq_description = db.Column(db.Text)

class Option(db.Model):
    opt_id = db.Column(db.Integer, primary_key=True)
    id_enquete = db.Column(db.Integer, db.ForeignKey('enquete.enq_id'), nullable=False)
    opt_description = db.Column(db.Text, nullable=False)

class Voto(db.Model):
    vt_id = db.Column(db.Integer, primary_key=True)
    id_enquete = db.Column(db.Integer, db.ForeignKey('enquete.enq_id'), nullable=False)
    id_option = db.Column(db.Integer, db.ForeignKey('option.opt_id'), nullable=False)

# Aqui estou criando um Endpoint para criar uma nova enquete
@app.route('/api/enquetes', methods=['POST'])
def create_enquete():
    data = request.get_json()
    if 'enq_title' not in data:
        return jsonify({"message": "Faltando 'enq_title' na solicitação"}), 400

    new_enquete = Enquete(enq_title=data['enq_title'], enq_description=data.get('enq_description'))
    db.session.add(new_enquete)
    db.session.commit()
    return jsonify({"message": "Enquete created successfully", "enq_id": new_enquete.enq_id}), 201

# Aqui estou criando um Endpoint para obter uma lista de enquetes
@app.route('/api/enquetes', methods=['GET'])
def list_enquetes():
    enquetes = Enquete.query.all()
    enquetes_data = [{"enq_id": enquete.enq_id, "enq_title": enquete.enq_title, "enq_description": enquete.enq_description} for enquete in enquetes]
    return jsonify(enquetes_data)

# Aqui estou criando um Endpoint para obter uma enquete
@app.route('/api/enquetes/<int:enq_id>', methods=['GET'])
def get_enquete(enq_id):
    enquete = Enquete.query.get(enq_id)
    if enquete:
        enquete_data = {"enq_id": enquete.enq_id, "enq_title": enquete.enq_title, "enq_description": enquete.enq_description}
        return jsonify(enquete_data)
    else:
        return jsonify({"message": "Enquete not found"}), 404

# Aqui estou criando um Endpoint para atualizar uma enquete
@app.route('/api/enquetes/<int:enq_id>/votar', methods=['POST'])
def vote_enquete(enq_id):
    data = request.get_json()
    if 'option_id' not in data:
        return jsonify({"message": "Missing 'option_id' in request"}), 400

    option_id = data['option_id']
    option = Option.query.get(option_id)
    if option and option.id_enquete == enq_id:
        new_vote = Voto(id_enquete=enq_id, id_option=option_id)
        db.session.add(new_vote)
        db.session.commit()
        return jsonify({"message": "Vote added successfully"}), 201
    else:
        return jsonify({"message": "Option not found or does not belong to the specified enquete"}), 404

# Aqui estou criando um Endpoint para obter os resultados de uma enquete
@app.route('/api/enquetes/<int:enq_id>/resultados', methods=['GET'])
def get_enquete_results(enq_id):
    enquete = Enquete.query.get(enq_id)
    if enquete:
        options = Option.query.filter_by(id_enquete=enq_id).all()
        results = {}
        for option in options:
            vote_count = Voto.query.filter_by(id_option=option.opt_id).count()
            results[option.opt_id] = {"opt_description": option.opt_description, "vote_count": vote_count}
        return jsonify(results)
    else:
        return jsonify({"message": "Enquete not found"}), 404

# Aqui estou criando um Endpoint para obter as opções de uma enquete
@app.route('/api/enquetes/<int:enq_id>/opcoes', methods=['GET'])
def get_enquete_options(enq_id):
    options = Option.query.filter_by(id_enquete=enq_id).all()
    options_data = [{"opt_id": option.opt_id, "opt_description": option.opt_description} for option in options]
    return jsonify(options_data)

# Aqui estou criando um Endpoint para adicionar uma nova opção a uma enquete
@app.route('/api/enquetes/<int:enq_id>/opcoes', methods=['POST'])
def add_option(enq_id):
    data = request.get_json()
    if 'opt_description' not in data:
        return jsonify({"message": "Missing 'opt_description' in request"}), 400

    new_option = Option(id_enquete=enq_id, opt_description=data['opt_description'])
    db.session.add(new_option)
    db.session.commit()
    return jsonify({"message": "Option added successfully", "opt_id": new_option.opt_id}), 201

# Aqui estou criando um Endpoint para atualizar uma opção de uma enquete
@app.route('/api/enquetes/<int:enq_id>', methods=['DELETE'])
def delete_enquete(enq_id):
    enquete = Enquete.query.get(enq_id)
    if enquete:
        db.session.delete(enquete)
        db.session.commit()
        return jsonify({"message": "Enquete deleted successfully"}), 200
    else:
        return jsonify({"message": "Enquete not found"}), 404

# Aqui estou criando um Endpoint para excluir uma opção de uma enquete
@app.route('/api/enquetes/<int:enq_id>/opcoes/<int:opt_id>', methods=['DELETE'])
def delete_option(enq_id, opt_id):
    option = Option.query.filter_by(id_enquete=enq_id, opt_id=opt_id).first()
    if option:
        db.session.delete(option)
        db.session.commit()
        return jsonify({"message": "Option deleted successfully"}), 200
    else:
        return jsonify({"message": "Option not found"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
