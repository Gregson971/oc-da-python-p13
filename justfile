# Run all test and coverage
test-all:
    pytest --cov --cov-config=.coveragerc --cov-fail-under=80

# Run linter
lint:
    flake8 --max-line-length=99 --exclude='**/migrations/*,venv'

# Build a Docker image
build-image:
    docker build -t gregson971/oc-da-python-p13 .

# Push a Docker image
push-image:
    docker push gregson971/oc-da-python-p13

# Build and run the application with Compose
run:
    docker-compose up

# Generate assets
assets:
    python3 manage.py collectstatic --noinput --clear
