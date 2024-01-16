from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def calculate_kmeans(embeddings, number_of_clusters, seed=None):
    kmeans = KMeans(n_clusters=number_of_clusters, random_state=seed)
    kmeans.fit(embeddings)
    clusters = kmeans.predict(embeddings)
    return kmeans, clusters

def calculate_silhouette_scores(embeddings, min_number_of_clusters, max_number_of_clusters, seed=None):
    silhouette_scores = []
    for number_of_clusters in range(min_number_of_clusters, max_number_of_clusters+1):
        kmeans, clusters = calculate_kmeans(embeddings, number_of_clusters, seed)
        silhouette_scores.append(silhouette_score(embeddings, clusters))
    return silhouette_scores