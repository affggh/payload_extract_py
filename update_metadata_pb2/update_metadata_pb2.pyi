from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApexInfo(_message.Message):
    __slots__ = ["decompressed_size", "is_compressed", "package_name", "version"]
    DECOMPRESSED_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    decompressed_size: int
    is_compressed: bool
    package_name: str
    version: int
    def __init__(self, package_name: _Optional[str] = ..., version: _Optional[int] = ..., is_compressed: bool = ..., decompressed_size: _Optional[int] = ...) -> None: ...

class ApexMetadata(_message.Message):
    __slots__ = ["apex_info"]
    APEX_INFO_FIELD_NUMBER: _ClassVar[int]
    apex_info: _containers.RepeatedCompositeFieldContainer[ApexInfo]
    def __init__(self, apex_info: _Optional[_Iterable[_Union[ApexInfo, _Mapping]]] = ...) -> None: ...

class CowMergeOperation(_message.Message):
    __slots__ = ["dst_extent", "src_extent", "src_offset", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    COW_COPY: CowMergeOperation.Type
    COW_REPLACE: CowMergeOperation.Type
    COW_XOR: CowMergeOperation.Type
    DST_EXTENT_FIELD_NUMBER: _ClassVar[int]
    SRC_EXTENT_FIELD_NUMBER: _ClassVar[int]
    SRC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    dst_extent: Extent
    src_extent: Extent
    src_offset: int
    type: CowMergeOperation.Type
    def __init__(self, type: _Optional[_Union[CowMergeOperation.Type, str]] = ..., src_extent: _Optional[_Union[Extent, _Mapping]] = ..., dst_extent: _Optional[_Union[Extent, _Mapping]] = ..., src_offset: _Optional[int] = ...) -> None: ...

class DeltaArchiveManifest(_message.Message):
    __slots__ = ["apex_info", "block_size", "dynamic_partition_metadata", "max_timestamp", "minor_version", "partial_update", "partitions", "security_patch_level", "signatures_offset", "signatures_size"]
    APEX_INFO_FIELD_NUMBER: _ClassVar[int]
    BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_PARTITION_METADATA_FIELD_NUMBER: _ClassVar[int]
    MAX_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_UPDATE_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_PATCH_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_SIZE_FIELD_NUMBER: _ClassVar[int]
    apex_info: _containers.RepeatedCompositeFieldContainer[ApexInfo]
    block_size: int
    dynamic_partition_metadata: DynamicPartitionMetadata
    max_timestamp: int
    minor_version: int
    partial_update: bool
    partitions: _containers.RepeatedCompositeFieldContainer[PartitionUpdate]
    security_patch_level: str
    signatures_offset: int
    signatures_size: int
    def __init__(self, block_size: _Optional[int] = ..., signatures_offset: _Optional[int] = ..., signatures_size: _Optional[int] = ..., minor_version: _Optional[int] = ..., partitions: _Optional[_Iterable[_Union[PartitionUpdate, _Mapping]]] = ..., max_timestamp: _Optional[int] = ..., dynamic_partition_metadata: _Optional[_Union[DynamicPartitionMetadata, _Mapping]] = ..., partial_update: bool = ..., apex_info: _Optional[_Iterable[_Union[ApexInfo, _Mapping]]] = ..., security_patch_level: _Optional[str] = ...) -> None: ...

class DynamicPartitionGroup(_message.Message):
    __slots__ = ["name", "partition_names", "size"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAMES_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    partition_names: _containers.RepeatedScalarFieldContainer[str]
    size: int
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ..., partition_names: _Optional[_Iterable[str]] = ...) -> None: ...

class DynamicPartitionMetadata(_message.Message):
    __slots__ = ["cow_version", "groups", "snapshot_enabled", "vabc_compression_param", "vabc_enabled", "vabc_feature_set"]
    COW_VERSION_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VABC_COMPRESSION_PARAM_FIELD_NUMBER: _ClassVar[int]
    VABC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VABC_FEATURE_SET_FIELD_NUMBER: _ClassVar[int]
    cow_version: int
    groups: _containers.RepeatedCompositeFieldContainer[DynamicPartitionGroup]
    snapshot_enabled: bool
    vabc_compression_param: str
    vabc_enabled: bool
    vabc_feature_set: VABCFeatureSet
    def __init__(self, groups: _Optional[_Iterable[_Union[DynamicPartitionGroup, _Mapping]]] = ..., snapshot_enabled: bool = ..., vabc_enabled: bool = ..., vabc_compression_param: _Optional[str] = ..., cow_version: _Optional[int] = ..., vabc_feature_set: _Optional[_Union[VABCFeatureSet, _Mapping]] = ...) -> None: ...

class Extent(_message.Message):
    __slots__ = ["num_blocks", "start_block"]
    NUM_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    START_BLOCK_FIELD_NUMBER: _ClassVar[int]
    num_blocks: int
    start_block: int
    def __init__(self, start_block: _Optional[int] = ..., num_blocks: _Optional[int] = ...) -> None: ...

class InstallOperation(_message.Message):
    __slots__ = ["data_length", "data_offset", "data_sha256_hash", "dst_extents", "dst_length", "src_extents", "src_length", "src_sha256_hash", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BROTLI_BSDIFF: InstallOperation.Type
    BSDIFF: InstallOperation.Type
    DATA_LENGTH_FIELD_NUMBER: _ClassVar[int]
    DATA_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
    DISCARD: InstallOperation.Type
    DST_EXTENTS_FIELD_NUMBER: _ClassVar[int]
    DST_LENGTH_FIELD_NUMBER: _ClassVar[int]
    LZ4DIFF_BSDIFF: InstallOperation.Type
    LZ4DIFF_PUFFDIFF: InstallOperation.Type
    MOVE: InstallOperation.Type
    PUFFDIFF: InstallOperation.Type
    REPLACE: InstallOperation.Type
    REPLACE_BZ: InstallOperation.Type
    REPLACE_XZ: InstallOperation.Type
    SOURCE_BSDIFF: InstallOperation.Type
    SOURCE_COPY: InstallOperation.Type
    SRC_EXTENTS_FIELD_NUMBER: _ClassVar[int]
    SRC_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SRC_SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ZERO: InstallOperation.Type
    ZUCCHINI: InstallOperation.Type
    data_length: int
    data_offset: int
    data_sha256_hash: bytes
    dst_extents: _containers.RepeatedCompositeFieldContainer[Extent]
    dst_length: int
    src_extents: _containers.RepeatedCompositeFieldContainer[Extent]
    src_length: int
    src_sha256_hash: bytes
    type: InstallOperation.Type
    def __init__(self, type: _Optional[_Union[InstallOperation.Type, str]] = ..., data_offset: _Optional[int] = ..., data_length: _Optional[int] = ..., src_extents: _Optional[_Iterable[_Union[Extent, _Mapping]]] = ..., src_length: _Optional[int] = ..., dst_extents: _Optional[_Iterable[_Union[Extent, _Mapping]]] = ..., dst_length: _Optional[int] = ..., data_sha256_hash: _Optional[bytes] = ..., src_sha256_hash: _Optional[bytes] = ...) -> None: ...

class PartitionInfo(_message.Message):
    __slots__ = ["hash", "size"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    size: int
    def __init__(self, size: _Optional[int] = ..., hash: _Optional[bytes] = ...) -> None: ...

class PartitionUpdate(_message.Message):
    __slots__ = ["estimate_cow_size", "fec_data_extent", "fec_extent", "fec_roots", "filesystem_type", "hash_tree_algorithm", "hash_tree_data_extent", "hash_tree_extent", "hash_tree_salt", "merge_operations", "new_partition_info", "new_partition_signature", "old_partition_info", "operations", "partition_name", "postinstall_optional", "postinstall_path", "run_postinstall", "version"]
    ESTIMATE_COW_SIZE_FIELD_NUMBER: _ClassVar[int]
    FEC_DATA_EXTENT_FIELD_NUMBER: _ClassVar[int]
    FEC_EXTENT_FIELD_NUMBER: _ClassVar[int]
    FEC_ROOTS_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    HASH_TREE_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    HASH_TREE_DATA_EXTENT_FIELD_NUMBER: _ClassVar[int]
    HASH_TREE_EXTENT_FIELD_NUMBER: _ClassVar[int]
    HASH_TREE_SALT_FIELD_NUMBER: _ClassVar[int]
    MERGE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEW_PARTITION_INFO_FIELD_NUMBER: _ClassVar[int]
    NEW_PARTITION_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    OLD_PARTITION_INFO_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    POSTINSTALL_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    POSTINSTALL_PATH_FIELD_NUMBER: _ClassVar[int]
    RUN_POSTINSTALL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    estimate_cow_size: int
    fec_data_extent: Extent
    fec_extent: Extent
    fec_roots: int
    filesystem_type: str
    hash_tree_algorithm: str
    hash_tree_data_extent: Extent
    hash_tree_extent: Extent
    hash_tree_salt: bytes
    merge_operations: _containers.RepeatedCompositeFieldContainer[CowMergeOperation]
    new_partition_info: PartitionInfo
    new_partition_signature: _containers.RepeatedCompositeFieldContainer[Signatures.Signature]
    old_partition_info: PartitionInfo
    operations: _containers.RepeatedCompositeFieldContainer[InstallOperation]
    partition_name: str
    postinstall_optional: bool
    postinstall_path: str
    run_postinstall: bool
    version: str
    def __init__(self, partition_name: _Optional[str] = ..., run_postinstall: bool = ..., postinstall_path: _Optional[str] = ..., filesystem_type: _Optional[str] = ..., new_partition_signature: _Optional[_Iterable[_Union[Signatures.Signature, _Mapping]]] = ..., old_partition_info: _Optional[_Union[PartitionInfo, _Mapping]] = ..., new_partition_info: _Optional[_Union[PartitionInfo, _Mapping]] = ..., operations: _Optional[_Iterable[_Union[InstallOperation, _Mapping]]] = ..., postinstall_optional: bool = ..., hash_tree_data_extent: _Optional[_Union[Extent, _Mapping]] = ..., hash_tree_extent: _Optional[_Union[Extent, _Mapping]] = ..., hash_tree_algorithm: _Optional[str] = ..., hash_tree_salt: _Optional[bytes] = ..., fec_data_extent: _Optional[_Union[Extent, _Mapping]] = ..., fec_extent: _Optional[_Union[Extent, _Mapping]] = ..., fec_roots: _Optional[int] = ..., version: _Optional[str] = ..., merge_operations: _Optional[_Iterable[_Union[CowMergeOperation, _Mapping]]] = ..., estimate_cow_size: _Optional[int] = ...) -> None: ...

class Signatures(_message.Message):
    __slots__ = ["signatures"]
    class Signature(_message.Message):
        __slots__ = ["data", "unpadded_signature_size", "version"]
        DATA_FIELD_NUMBER: _ClassVar[int]
        UNPADDED_SIGNATURE_SIZE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        unpadded_signature_size: int
        version: int
        def __init__(self, version: _Optional[int] = ..., data: _Optional[bytes] = ..., unpadded_signature_size: _Optional[int] = ...) -> None: ...
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    signatures: _containers.RepeatedCompositeFieldContainer[Signatures.Signature]
    def __init__(self, signatures: _Optional[_Iterable[_Union[Signatures.Signature, _Mapping]]] = ...) -> None: ...

class VABCFeatureSet(_message.Message):
    __slots__ = ["batch_writes", "threaded"]
    BATCH_WRITES_FIELD_NUMBER: _ClassVar[int]
    THREADED_FIELD_NUMBER: _ClassVar[int]
    batch_writes: bool
    threaded: bool
    def __init__(self, threaded: bool = ..., batch_writes: bool = ...) -> None: ...
