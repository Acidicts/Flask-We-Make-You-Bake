import Website

app = Website.create_app()
app.run(debug=True, host='0.0.0.0', port=5000)
