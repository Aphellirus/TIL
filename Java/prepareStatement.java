String sql=Insert into accounts(username, password) values (?,?);
PreparedStatement stmt = connection.prepareStatement(sql);
stmt.setString(1, usuario);
stmt.setString(2, senha);
stmt.execute();
