# serializers.py
from rest_framework import serializers
from .models import Director, Movie, Review

# serializers.py

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя режиссера не может быть пустым.")
        if Director.objects.filter(name=value).exists():
            raise serializers.ValidationError("Режиссер с таким именем уже существует.")
        return value

# serializers.py

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название фильма не может быть пустым.")
        if Movie.objects.filter(title=value).exists():
            raise serializers.ValidationError("Фильм с таким названием уже существует.")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Описание фильма должно содержать не менее 10 символов.")
        return value


# serializers.py

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_stars(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Оценка должна быть в диапазоне от 1 до 5.")
        return value

    def validate_content(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Отзыв должен содержать не менее 5 символов.")
        return value

    def validate(self, data):
        if Review.objects.filter(movie=data['movie'], content=data['content']).exists():
            raise serializers.ValidationError("Такой отзыв для данного фильма уже существует.")
        return data
